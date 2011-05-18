function showOnMenu(elem,image)
{
    path = '/media/images/';
    elem.src = path + image;
}

function MM_preloadImages() { //v3.0
    var d=document; 
    if(d.images){ 
        if(!d.MM_p) d.MM_p=new Array();
        var i,j=d.MM_p.length,a=MM_preloadImages.arguments; 
        for(i=0; i<a.length; i++) {
            if (a[i].indexOf("#")!=0){ 
                d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];
            }
        }
    }
}

function MM_randomImages() {
    var img_name = new Array("templates/Company/images/home/oxford-summer-school-1.jpg", "templates/Company/images/home/oxford-summer-school-2.jpg", "templates/Company/images/home/oxford-summer-school-3.jpg", "templates/Company/images/home/oxford-summer-school-4.jpg", "templates/Company/images/home/oxford-summer-school-5.jpg", "templates/Company/images/home/oxford-summer-school-6.jpg");
    var l = img_name.length;
    var rnd_no = Math.floor(l*Math.random());
    var rnd_num = parseInt(rnd_no) +1;
    document.getElementById("slideshow").innerHTML = '<a href="http://www.oxford-royale.co.uk/summer-courses-in-oxford-and-cambridge.html" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage(\'im_'+rnd_num+'\',\'\',\'http://www.oxford-royale.co.uk/templates/Company/images/home/oxford-summer-school-'+rnd_num+'R.jpg\',1)"><img name="im_'+rnd_num+'" src="'+img_name[rnd_no]+'" border="0" id="im_'+rnd_num+'">';
}

$(document).ready(function(){
    MM_randomImages();
    MM_preloadImages('/media/images/top1.jpg','/media/images/top2.jpg','/media/images/1c.jpg');
});
