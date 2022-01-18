from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .models import AddBus,Passenger,Seat

def index(request):
    return render(request, 'Home.html')

# def about(request):
#     return HttpResponse("this is about us.")

def contact(request):
    return render(request,'contact.html')

# def service(request):
#     return HttpResponse("This is service page.")

def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def PassInfo(request):
    pas=Passenger.objects.filter()
    return render(request,'PassInfo.html',{'pas':pas})

@login_required(login_url='login')
def deletehistory(request,pk):
    del_his=Passenger.objects.get(pk=pk)
    del_his.delete()
    print("History deleted!")
    log_user=request.user
    passen=Passenger.objects.filter(Uname=log_user)
    print(passen)
    # print(passen.Fname)
    return render(request, 'history.html',{"passen":passen,"user":log_user})


@login_required(login_url='login')
def history(request):
    log_user=request.user
    passen=Passenger.objects.filter(Uname=log_user)
    print(passen)
    # print(passen.Fname)
    return render(request, 'history.html',{"passen":passen,"user":log_user})

@login_required(login_url='login')
def book_Bus(request,name,pick,dest,ptime,dtime,fare,bustype,date):
    # book_Bus=AddBus.objects.get(pk=pk)
    print(name)
    print(fare)
    print(pick)
    print(dest)
    print(ptime)
    print(dtime)
    print(bustype)
    print(date)
    passenger=Passenger()
    seat=Seat.objects.filter(busName=name)
    print(seat)
    seat1=[]
    seat2=[]
    seat3=[]
    seat4=[]
    for i in range(12):
        seat1.append(seat[i])
    for i in range(12,24):
        seat2.append(seat[i])
    for i in range(24,36):
        seat3.append(seat[i])
    for i in range(36,48):
        seat4.append(seat[i])
    # print(seat1)
    # print("\nhello")
    # print(seat2)
    # print("\nhello")
    # print(seat3)
    # print("\nhello")
    # print(seat4)
        
    if request.method=='POST':
        Uname=request.user
        Fname = request.POST['Fname']
        Phoneno=request.POST['Phoneno']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        seatNum=request.POST['seatNum']
        passenger.busName=name
        passenger.source=pick
        passenger.destination=dest
        passenger.stime=ptime
        passenger.dtime=dtime
        passenger.totFare=fare
        passenger.busType=bustype
        passenger.date=date
        passenger.Uname=Uname
        passenger.Fname=Fname
        passenger.Phoneno=Phoneno
        passenger.email=email
        passenger.age=age
        passenger.gender=gender
        passenger.seatNum=seatNum
        
        passenger.save()
        obj=Seat.objects.filter(busName=name,seatNo=seatNum)
        obj.update(seatStatus=True)
        # if(request.method == 'POST'):
        #     no= request.POST.get('no') #11
        #     print("hello krupali")
        #     return HttpResponse(no)
        # p=Passenger.objects.filter()
        template=render_to_string('email.html',{'p':passenger})
        email=EmailMessage(
        'Booking Confirmation!',
        template,
        settings.EMAIL_HOST_USER,
        [email],
        print(email)
        )
        email.send()
        from twilio.rest import Client

        # Find these values at https://twilio.com/user/account
        # To set up environmental variables, see http://twil.io/secure
        account_sid = 'ACbf1f78990d1304ef8aee5df607552e68'
        auth_token = 'e153fe68da8ee02c6f662783df0ce155'

        client = Client(account_sid, auth_token)

        msg=client.messages.create(
            to='+918849552209',
            from_='+1 205 843 6631',
            body=template)
        print(msg.sid)
        return render(request, 'home.html')

    return render(request, 'Seat-layout.html',{"name":name,"seat1":seat1,"seat2":seat2,"seat3":seat3,"seat4":seat4})

# def seat_no(request):
#     if(request.method == 'POST'):
#         no= request.POST.get('no') #11
#         print("hello krupali")
#     return HttpResponse(no)

def trackBus(request):
    import requests
    import folium
    res=requests.get('https://ipinfo.io/')

    # res.raise_for_status()  # raises exception when not a 2xx response
    # if res.status_code != 204:
    #     data=res.json()
    print(res)
    data=res.json()
    print(data)
    loaction=data['loc'].split(',')
    lat=float(loaction[0])
    log=float(loaction[1])

    fg=folium.FeatureGroup("my map")
    # fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

    fg.add_child(folium.Marker(location=[lat,log],popup="Ahmedabad"))

    map=folium.Map(location=[lat,log],zoom_start=12)

    map.add_child(fg)
    map.save("templates//map.html")


    # import geocoder
    # import folium
    # g=geocoder.ip("me")
    # myaddress=g.latlng
    # mymap=folium.Map(loaction=myaddress,zoom_start=5000)
    # folium.CircleMarker(location=myaddress,radius=50,popup="Morbi").add_to(mymap)
    # folium.Marker(myaddress,popup="Morbi").add_to(mymap)
    # mymap.save("templates//map.html")

    return render(request, 'map.html')



@login_required(login_url='login')
def book(request):
    if request.method=='POST':
        date=request.POST['date']
        pickup=request.POST['pickup']
        dest=request.POST['dest']
        add_Bus=AddBus.objects.filter()
        bname=[]
        pick=[]
        destination=[]
        picktime=[]
        desttime=[]
        pricelist=[]
        bus_type=[]
        Date=[]
        # bus=AddBus.objects.filter("PickUp":pickup,"dest":dest)
        for bus in add_Bus:
            
            if bus.PickUp == pickup or bus.dest==pickup or bus.s1name==pickup or bus.s2name==pickup or bus.s3name==pickup or bus.s4name==pickup:
                if bus.PickUp == dest or bus.dest==dest or bus.s1name==dest or bus.s2name==dest or bus.s3name==dest or bus.s4name==dest:
                
                    bus_list=[bus.PickUp,bus.s1name,bus.s2name,bus.s3name,bus.s4name,bus.dest]
                    price_list=[0,bus.s1fare,bus.s2fare,bus.s3fare,bus.s4fare,bus.fare]
                    time_list=[bus.ptime,bus.s1time,bus.s2time,bus.s3time,bus.s4time,bus.dtime]
                    print(bus_list)
                    bname.append(bus.Bname)
                    print(price_list)
                    print(pickup)
                    pick.append(pickup)
                    print(dest)
                    destination.append(dest)
                    pick_index=bus_list.index(pickup)
                    dest_index=bus_list.index(dest)
                    pick_time=time_list[pick_index]
                    dest_time=time_list[dest_index]
                    picktime.append(pick_time)
                    desttime.append(dest_time)
                    print(pick_index)
                    print(dest_index)
                    flag=False
                    if pick_index!=(len(bus_list)-1):
                        for i in bus_list[pick_index+1:]:
                            if dest in i:
                                flag=True
                                print("5")
                                price=sum(price_list[pick_index+1:dest_index+1])
                                pricelist.append(price)
                                bus_type.append(bus.Btype)
                                Date.append(date)
                                print(f'price:{price}')
                                break
                            else:
                                print("4")
                                flag=False
                    #             print("bus not available")
                    else:
                        print("3")
                        flag=False
                    #     print("bus not available")
                    if flag:
                        print("1")
                        print("bus available")
                    else:
                        print("2")
                        print("bus not available")
        print(bus_type)
        print(Date)
        # print(date.toString())
        # mylist=zip(bname,pick,destination,picktime,desttime,pricelist)
        zipp=zip(bname,pick,destination,picktime,desttime,pricelist,bus_type,Date)
        # # mylist=zip(bname,pick)
        # print(list(zipp))
        # print("condition")
        # data = {
        #     'mylist': zipp,
        # }
        return render(request, 'Bus-list.html',{"zipp":zipp})           
    else:
        print("noncondition")
        return render(request, 'Bus-list.html')

@login_required(login_url='login')
def admin(request):
    if request.user.is_superuser:
        add_Bus=AddBus.objects.filter()
        if request.method=='POST':
            addBus=AddBus()
            Bname = request.POST['Bname']
            PickUp=request.POST['PickUp']
            ptime=request.POST['ptime']
            dest=request.POST['dest']
            dtime=request.POST['dtime']
            s1name=request.POST['s1name']
            s1time=request.POST['s1time']
            s1fare=request.POST['s1fare']
            s2name=request.POST['s2name']
            s2time=request.POST['s2time']
            s2fare=request.POST['s2fare']
            s3name=request.POST['s3name']
            s3time=request.POST['s3time']
            s3fare=request.POST['s3fare']
            s4name=request.POST['s4name']
            s4time=request.POST['s4time']
            s4fare=request.POST['s4fare']
            Btype=request.POST['btype']
            fare=request.POST['fare']


            addBus.Bname = Bname
            addBus.PickUp=PickUp
            addBus.ptime=ptime
            addBus.dest=dest
            addBus.dtime=dtime
            addBus.s1name=s1name
            addBus.s1time=s1time
            addBus.s1fare=s1fare
            addBus.s2name=s2name
            addBus.s2time=s2time
            addBus.s2fare=s2fare
            addBus.s3name=s3name
            addBus.s3time=s3time
            addBus.s3fare=s3fare
            addBus.s4name=s4name
            addBus.s4time=s4time
            addBus.s4fare=s4fare
            addBus.Btype=Btype
            addBus.fare=fare

            addBus.save()
            print("Data Saved!")
            # print(addBus)
            messages.success(request,'Data Saved Successfully!')
            posts = AddBus.objects.all() 
            total_fare=[]
            for post in posts: 
                tot_fare=post.s1fare + post.s2fare + post.s3fare + post.s4fare +post.fare
                total_fare.append(tot_fare)
                print(tot_fare)

            print(total_fare)
            zipp=zip(add_Bus,total_fare)
            print(zipp)
            return render(request, 'admin.html',{"items":zipp })
            # return render(request, 'admin.html',{"addBus":add_Bus})
        else:    
            # print(addBus)
            # tot_fare=AddBus.objects.annotate(sum(s1fare,s2fare))
            # tot_fare=AddBus.objects.annotate(sum('tot_fare','s3fare'))
            # tot_fare=AddBus.objects.annotate(sum('tot_fare','s4fare'))
            # tot_fare=AddBus.objects.annotate(sum('tot_fare','fare'))
            # print(AddBus.objects.filter('s1fare'))
            # tot_fare=sum(int(AddBus.objects.filter('s1fare','s2fare','s3fare','s4fare','fare')))

            posts = AddBus.objects.all() 
            total_fare=[]
            for post in posts: 
                tot_fare=post.s1fare + post.s2fare + post.s3fare + post.s4fare +post.fare
                total_fare.append(tot_fare)
                print(tot_fare)

            print(total_fare)
            zipp=zip(add_Bus,total_fare)
            print(zipp)
            return render(request, 'admin.html',{"items":zipp })
    else:
        return HttpResponse("Only Admin can acess this page")
        


@login_required(login_url='login')
def deleteBus(request,pk):
    if request.user.is_superuser:
        add_Bus=AddBus.objects.filter()
        print(pk)
        del_Bus=AddBus.objects.get(pk=pk)
        del_Bus.delete()
        print("Bus deleted!")
        posts = AddBus.objects.all() 
        total_fare=[]
        for post in posts: 
            tot_fare=post.s1fare + post.s2fare + post.s3fare + post.s4fare +post.fare
            total_fare.append(tot_fare)
            print(tot_fare)

        print(total_fare)
        zipp=zip(add_Bus,total_fare)
        print(zipp)
        return render(request, 'admin.html',{"items":zipp })
    else:
        return HttpResponse("Only Admin can acess this page")
    # return render(request, 'admin.html',{"addBus":add_Bus})

def sign_up(request):

    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']

        if password==c_password:
            
            if User.objects.filter(username=name).exists():
                print("username taken!")
                messages.error(request,'Username taken!')
                return render(request,'sign-up.html')
            elif User.objects.filter(email=email).exists():
                print("email taken!")
                messages.error(request,'Already registred with same email!')
                return render(request,'sign-up.html')
            else:
                user=User.objects.create_user(username=name,password=password,email=email)
                user.save();
                messages.success(request,'Account Created Successfully!')
                print("user created")
                return render(request,'login.html')
        else:
            messages.error(request,'Password not matching!')
            print("password not matching!")
            return render(request,'sign-up.html')

    else:
        return render(request,'sign-up.html')

def login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        print(username)
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("logedin!")

            return render(request,'Home.html')
        else:
            print('invalid credentials!')
            messages.error(request,'Invalid credentials!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
