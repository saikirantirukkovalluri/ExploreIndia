from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import StatesData,Loc
import folium
from folium.plugins import Fullscreen
import geocoder


def home(request):
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5,min_zoom=2,max_bounds=False,titles='Explore India')
    Fullscreen(position='topright',title='FULL_SCREEN',title_cancel='Exit_Screen',force_seperate_button=True).add_to(m)
    obj = Loc.objects.all()
    for i in obj:
        v=i.lat
        l=i.lon    
        folium.Marker(
        location=[v,l],
        popup='<a href="http://127.0.0.1:8000/state/'+str(i.id)+'" target="blank">'+str(i.statnam)+'</a>',icon=folium.Icon(color='green',prefix='glyphicon',icon='off'),max_bound=True,tooltip=str(i.statnam)).add_to(m)
        # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,            
    }
    return render(request,'thetianzu/index.html',context)

def state(request, id):
    data = StatesData.objects.get(id=id)
    return render(request,'thetianzu/state.html',{'record':data})
def aboutus(request):
    if request.method =="POST":
        emai=request.POST['email']
        passw=request.POST['feedback']
        e='sivaramgandi1468@gmail.com'
        print(emai,passw)
        send_mail("Feedback from "+emai,passw,"teamexploreindia05@gmail.com",[e],fail_silently=False)		
        send_mail("Thankyou For visiting our site","How did we do?\n \nWe hope you enjoy Explore India and that you find it's insightful and easy to use.\n \n \nWe want to be better ,and your feedback helps us accomplish that and will help us to make Explore India an accurate \n \n \n \n \n \nThanks for your help!\n \nteam ExploreIndia\n \n \n \n \n \nContact us\n \n \n teamexploreindia05@gmail.com","teamexploreindia05@gmail.com",[emai],fail_silently=False)
		

    return render(request,'thetianzu/aboutus.html')