from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug":"ethical-hacking",
        "image":"download.png",
        "author":"hiral-tarpara",
        "date": date(2022, 8, 20),
        "title":"Ethical hacking",
        "excerpt":"Ethical hacking involves an authorized attempt to gain unauthorized access to a computer system, application, or data. ",
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quae distinctio consequuntur inventore earum! Accusamus sapiente earum 
        vitae quod deleniti! Placeat nam deserunt ea amet voluptates asperiores
         iste voluptate, animi iure!

         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quae distinctio consequuntur inventore earum! Accusamus sapiente earum 
        vitae quod deleniti! Placeat nam deserunt ea amet voluptates asperiores
         iste voluptate, animi iure!
        """
    },
    {
        "slug":"machine-learning",
        "image":"main2.jpg",
        "author":"hiral-tarpara",
        "date": date(2022, 11, 20),
        "title":"machine learning",
        "excerpt":"Ethical hacking involves an authorized attempt to gain unauthorized access to a computer system, application, or data. ",
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quae distinctio consequuntur inventore earum! Accusamus sapiente earum 
        vitae quod deleniti! Placeat nam deserunt ea amet voluptates asperiores
         iste voluptate, animi iure!

         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quae distinctio consequuntur inventore earum! Accusamus sapiente earum 
        vitae quod deleniti! Placeat nam deserunt ea amet voluptates asperiores
         iste voluptate, animi iure!

         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quae distinctio consequuntur inventore earum! Accusamus sapiente earum 
        vitae quod deleniti! Placeat nam deserunt ea amet voluptates asperiores
         iste voluptate, animi iure!
        """
    },
    {
        "slug":"computer-science",
        "image":"images.jpeg",
        "author":"hiral-tarpara",
        "date": date(2022, 9, 22),
        "title":"computer science",
        "excerpt":"Ethical hacking involves an authorized attempt to gain unauthorized access to a computer system, application, or data. ",
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quae distinctio consequuntur inventore earum! Accusamus sapiente earum 
        vitae quod deleniti! Placeat nam deserunt ea amet voluptates asperiores
         iste voluptate, animi iure!

        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{ 
        "posts":latest_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts": all_posts  
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{
        "post": identified_post
    })