from flet import *
from utils.extras import *
import time
import random
from threading import Thread
import flet as ft
bgcolor1='#f5c000'
bgcolor2='#5525c9',

#import flet as ft

pgw=0.0
pgh=0.0
bigcardoption1 = ['A1-Pages','Home','About us','Pricing','Integration']
bigcardoption2 = ['A1-Utilty Page','Log In','Sign Up','Reset Password','Reset Password']
bigcardoption3 = ['A1-CMS Page','Pricing Single','Integration Single','Career Details','Blog Details']
smallcardoption1 = ['Home1','Home2']
home_click_st = False
ttsize1,ttsize2,ttsize3,ttsize4,ttsize5,lgs,ttsize10 = 0.0, 0.0, 0.0, 0.0,0.0,0.0,0.0

smallmenucard1 = Column()
bigmenucard1 = Column()
bigmenucard2 = Column()
bigmenucard3 = Column() 

st1 = """
    #
    def Hello_World():
        print("Grow Your Business With Our Saastech!")
        for i in range(5):
            print(i)
        return "Done1"
        """
        
st2 = """
  #
  def Why_Choose_uS():
      print("Have Everything You Need In One Software!")
      for i in range(5):
          print(i)
      return "Done1"
      """
        
st3 = """
      #
      def Learn_Coding():
          print("Coding has change my world!")
          for i in range(5):
              print(i)
          return "Done1"
          """
            
yyy = [st1,st2,st3]

st = """
    #
    def Hello_World():
        print("Grow Your Business With Our Saastech!")
        for i in range(5):
            print(i)
        return "Done1"
        """


class Index(Container):
  def __init__(self,switch_page,pg):

    super().__init__()
    self.offset = transform.Offset(0,0,)
    self.switch_page = switch_page
    self.pg = pg
    
    global pgh,pgw,ttsize1,ttsize2,ttsize3,ttsize4,ttsize5,logosize,lgs,ttsize10
    
    
    
    pgh = pg.window_height if pg.window_height != 0.0 else pg.height
    pgw = pg.window_width if pg.window_width != 0.0 else pg.width
    ttsize1 = int((pgw *1.2) / 100)
    ttsize2 = int((pgw *1.4) / 100)
    ttsize3 = int((pgw *1.5) / 100)
    ttsize4 = int((pgw *1.7) / 100)
    ttsize5 = int((pgw *2.2) / 100)
    ttsize10 = int((pgw *5) / 100)
    logosize = int((pgw *4.5) / 100)
    lgs =  int((pgw *15) / 100)
   
   
   
    print((ttsize5,ttsize2,ttsize1,logosize,lgs))
    
    
    base_height2 = (pgh * 58) / 100 
    print('start' + ' ' + str(base_height2) )
    base_width2 = (pgw * 35) / 100
    print('start' + ' ' + str(base_width2))
    
    
    def page_resize(e):
    
      global base_height2,base_width,pgh,pgw,ttsize1,ttsize2,ttsize3,ttsize4,ttsize5,logosize,lgs,ttsize10
      
      pgh = pg.window_height if pg.window_height != 0.0 else pg.height
      pgw = pg.window_width if pg.window_width != 0.0 else pg.width
      ttsize1 = int((pgw *1.1) / 100)
      ttsize2 = int((pgw *1.3) / 100)
      ttsize3 = int((pgw *1.4) / 100)
      ttsize4 = int((pgw *1.45) / 100)
      ttsize5 = int((pgw *1.5) / 100)
      ttsize10 = int((pgw *5) / 100)
      logosize = int((pgw *4.5) / 100)
      lgs =  int((pgw *15) / 100)
      hkpage.margin = margin.only(left=(pgw *35) / 100)
      hkhome.margin = margin.only(left=(pgw *25) / 100)
      homepages.height = pgh
      homepages.width = pgw
      #print('ti' + str((pgw *30) / 100))
      
      # self.content.update()
      
      self.pg.update()
   
      
   
   
      print((ttsize5,ttsize2,ttsize1,logosize,lgs))
    
      base_height2 = (pgh * 58) / 100 
      print('start2' + ' ' + str(base_height2) )
      base_width2 = (pgw * 35) / 100
      print('start2' + ' ' + str(base_width2))
    

    aborder_color = colors.BLACK
    aborder_width = 2

    avatar1 = Container(
        bgcolor=colors.RED,
        width=45,
        height=45,
        border_radius=50,
        border=Border(
            left=BorderSide(width=aborder_width, color=aborder_color),
            right=BorderSide(width=aborder_width, color=aborder_color),
            top=BorderSide(width=aborder_width, color=aborder_color),
            bottom=BorderSide(width=aborder_width, color=aborder_color),
        ),
        content=Image(src="https://example.com/avatar1.jpg", fit=ImageFit.COVER)
    )

    avatar2 = Container(
        bgcolor='#f5c000',
        width=45,
        height=45,
        border_radius=50,
        border=Border(
            left=BorderSide(width=aborder_width, color=aborder_color),
            right=BorderSide(width=aborder_width, color=aborder_color),
            top=BorderSide(width=aborder_width, color=aborder_color),
            bottom=BorderSide(width=aborder_width, color=aborder_color),
        ),
        left=35,  # Adjust the overlap by changing the left value
        content=Image(src="https://example.com/avatar2.jpg", fit=ImageFit.COVER)
    )

    avatar3 = Container(
        bgcolor='#5525c9',
        width=45,
        height=45,
        border_radius=50,
        border=Border(
              left=BorderSide(width=aborder_width, color=aborder_color),
              right=BorderSide(width=aborder_width, color=aborder_color),
              top=BorderSide(width=aborder_width, color=aborder_color),
              bottom=BorderSide(width=aborder_width, color=aborder_color),
          ),
        left=70,  # Adjust the overlap by changing the left value
        content=Image(src="https://example.com/avatar3.jpg", fit=ImageFit.COVER)
    )

    
    
    
    my_typewriter_text = Markdown('', selectable=True,extension_set="gitHubWeb",
              code_theme="atom-one-dark",
              code_style=TextStyle(font_family="Roboto Mono"),
              on_tap_link=lambda e: page.launch_url(e.data),)
    
    # my_typewriter_text = Text('', no_wrap=False)
    
    gentext = Container(
              content=Text(
                      spans=[
                          TextSpan(
                              "Grow Your Business With Our Saastech",
                              TextStyle(
                                  size=ttsize10,
                                  weight=FontWeight.BOLD,
                                  font_family='Poppins regular',
                                  foreground=Paint(
                                      gradient=PaintLinearGradient(
                                          (0, 20), (150, 20), [colors.BLACK, colors.BLACK]
                                      )
                                  ),
                              ),
                          ),
                      ],
                  )
              
            ),


    container5 = Container(
        width=400,
        height=400,
        margin=margin.only(20),
        #padding=25,
        
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=['#1f2937','#111827']
            # colors=[colors.WHITE,colors.WHITE60]
            #Much better bg color
        ),
        # blur = Blur(10,10,BlurTileMode.REPEATED),
        # shadow = BoxShadow(
        #     1,
        #     15,
        #     colors.BLUE_GREY_300,
        #     Offset(2,2),
        #     ShadowBlurStyle.OUTER,
        # ),
      
        border_radius=25,
        content=my_typewriter_text
    )

    gj = Column([container5])
    
    
    #self.pg.add(gj)
    
    
  

    
    
    
    def typ():
      
      st = random.choice(yyy)
      
      fj = len(st)
      effecting = False
      affecting = False

      def effect():
          nonlocal effecting
          for i in range(fj):
              partial_code = st[:i + 1]
              if "Done1" in  partial_code:
                  pass
                  #print('Hello World!')
              #print(partial_code)
              #highlighted_text = highlight(partial_code, PythonLexer(), TerminalFormatter())
              my_typewriter_text.value = f"```python\n{partial_code}\n```"
              my_typewriter_text.update()
              time.sleep(0.05)
          effecting = True
          # gentext.value = st
          # gentext.update()

      def affect():
          nonlocal affecting
          for i in range(fj, 0, -1):
              partial_code = st[:i - 1]
              #highlighted_text = highlight(partial_code, PythonLexer(), TerminalFormatter())
              my_typewriter_text.value = f"```python\n{partial_code}\n```"
              my_typewriter_text.update()
              time.sleep(0.05)
          affecting = True
          
      
      #page.add(gj)

      while True:
          if not effecting:
              effect()
          else:
              if not affecting:
                  affect()
                  
              else:
                  effecting = False
                  affecting = False
                  st = random.choice(yyy)
      
    
    
    def SideColumn():
        #just like any variable we set one to equal to a column widget
        NumberColumn = Column(
            controls=[
                 #let say we want to create a column of several numbers, say 1-30 depending on the height of the container
                 
            ]
             
        )
        
        for number in range(1,30):
           
          NumberColumn.controls.append(Text(number,color='white',size=12))
         
        return NumberColumn
    
    
    
    
    page1 = Column(
      
      controls=[
        
            Row(
              #spacing=5,
              
              alignment='spaceBetween',
              controls=[
                Container(
                  width = (pgw * 42) / 100,
                  height = (pgh * 80) / 100 ,
                  bgcolor='#000000',
                  content=Column(#alignment='spaceBetween',
                                 spacing='25',
                                 controls=[
                                    Container(
                                      content=Text(
                                              spans=[
                                                  TextSpan(
                                                      "Grow Your Business With Our Saastech",
                                                      TextStyle(
                                                          size=ttsize10,
                                                          weight=FontWeight.BOLD,
                                                          font_family='Poppins regular',
                                                          foreground=Paint(
                                                              gradient=PaintLinearGradient(
                                                                  (0, 20), (150, 20), [colors.WHITE, colors.WHITE]
                                                              )
                                                          ),
                                                      ),
                                                  ),
                                              ],
                                          )
                                      
                                    ),
                                    
                                    #gentext,
                                    
                                    Container(
                                      content=Text( 'Learn where your audience struggle as they navigate your digital business. Pair this understanding of the individual experience with powerful quantitative insights to inform your digital decisions.'
                                                   ,font_family='poppins regular'
                                         ,size=ttsize1,color=colors.WHITE,weight=FontWeight.W_100,
                                    )
                                    ),
                                    
                                    Container(
                                      content=Row(
                                        spacing = 25,
                                        controls=[
                                           FilledButton(
                                                  # "Get Started",
                                                    content=Text(
                                                        "Book A Demo",
                                                        size=ttsize3,  # Set the desired text size
                                                    ),
                                                    width=180,  # Set the desired width
                                                    height=55,  # Set the desired height
                                                    style=ButtonStyle(
                                                      # color= '#5525c9',
                                                        bgcolor = colors.WHITE,
                                                        overlay_color= '#f5c000',
                                                        shape=RoundedRectangleBorder(radius=10),
                                                        color={
                                                            MaterialState.HOVERED: colors.BLACK,
                                                            MaterialState.FOCUSED: colors.BLACK,
                                                            MaterialState.DEFAULT: colors.BLACK,
                                                        },
                                                        
                                            
                                                        ),
                              
                                                       ), 
                                           
                                           FilledButton(
                                                  # "Get Started",
                                                    content=Text(
                                                        "Start Free Trial",
                                                        size=ttsize3,  # Set the desired text size
                                                    ),
                                                    width=180,  # Set the desired width
                                                    height=55,  # Set the desired height
                                                    style=ButtonStyle(
                                                      # color= '#5525c9',
                                                        bgcolor = '#f5c000',
                                                        overlay_color= '#5525c9',
                                                        shape=RoundedRectangleBorder(radius=10),
                                                        color={
                                                            MaterialState.HOVERED: colors.WHITE,
                                                            MaterialState.FOCUSED: colors.WHITE,
                                                            MaterialState.DEFAULT: colors.BLACK,
                                                        },
                                                        
                                            
                                                        ),
                              
                                                       ),  
                                           
                                           
                                              
                                        ]
                                      )
                                    ),
                                    
                                    Container(

                                      #width=20,
                                      #bgcolor=colors.PURPLE,
                                      content=Stack(
                                              width=500,
                                              height=120,
                                              controls=[
                                                
                                                Container(
                                                  
                                                  #bgcolor=colors.ORANGE,
                                                  width=300,
                                                  top=10,
                                                  #height=125,
                                                  
                                                  
                                                  content=Stack(
                                                    [avatar1, avatar2, avatar3],
                                                    width=300,
                                                    #height=100,
                                                    alignment='center',
                                                )) , 
                                                  
                                                  Container(
                                                    left=125,
                                                    
                                                    
                                                    #bgcolor=colors.GREEN,
                                                    content=Column([
                                                    Container(
                                                      width=300,
                                                      height=25,
                                                      content=Text( 'Active Users'
                                                                    ,font_family='poppins regular'
                                                          ,size=18,color=colors.WHITE,weight=FontWeight.W_100,
                                                      )
                                                    ),
                                                    Container(
                                                      width=300,
                                                      height=50,
                                                      #bgcolor=colors.RED,
                                                      content=Text(
                                                          spans=[
                                                              TextSpan(
                                                                  "20K+",
                                                                  TextStyle(
                                                                      size=25,
                                                                      weight=FontWeight.BOLD,
                                                                      font_family='Poppins regular',
                                                                      foreground=Paint(
                                                                          gradient=PaintLinearGradient(
                                                                              (0, 20), (150, 20), [colors.WHITE, colors.WHITE]
                                                                          )
                                                                      ),
                                                                  ),
                                                              ),
                                                          ],
                                                      )
                                      
                                                    )
                                                  ])  )      
                                
                                    ]))
                                
                                
                                ]),
                  
                  
                     
                ),
                
                
                Container(
                  width = (pgw * 55) / 100,
                  height = pgh + (pgh * 20) / 100 ,
                  #bgcolor = colors.BLUE,
                  content=Stack(
                          controls=[
                            
                            
                            Container(
                              bgcolor='#5525c9',
                              top=140,
                              left=180,
                              right=20,
                              bottom=20,
                              border_radius=25,
                            ),
                            
                            Container(
                              #width=200,
                              top=100,
                              left=100,
                              right=160,
                              bottom=220,
                              #bgcolor='black',
                              #I want some gradient instead of solid color
                              gradient=LinearGradient(
                                  begin=alignment.bottom_left,
                                  end=alignment.top_right,
                                  colors=['#1f2937','#111827']
                                  #Much better bg color
                              ),
                              #i want rounded edge on all side of the container
                              border_radius=border_radius.all(20),
                              
                              #we need to add padding for here
                              padding=padding.only(top=12,left=18,right=18),
                              
                              #now i want to start with the inner part of the window
                              #and since we willl be going from top to bottom, we will be starting with Column
                              # so let pass a column control to the container content
                              content=Column(
                                  #so starting from top to bottom
                                  #we will need a row to place the three circles at the top left
                                  controls=[
                                      Row(
                                          #we can start by creating the three circles
                                          #we will do this using container
                                          # i want to change the spacing between the circles a little
                                          spacing=7,
                                          controls=[
                                            
                                              Container(
                                                  width=14,
                                                  height=14,
                                                  bgcolor=colors.RED_500,
                                                  #we need to make them in a ciecle shape
                                                  border_radius=border_radius.all(50),
                                                  
                                              ),
                                              Container(
                                                  width=14,
                                                  height=14,
                                                  bgcolor='#f5c000',
                                                  border_radius=border_radius.all(50),
                                         
                                              ),
                                              Container(
                                                  width=14,
                                                  height=14,
                                                  bgcolor='#5525c9',
                                                  border_radius=border_radius.all(50),
                                                  
                                              ),
                                              
                                            
                                          ]
                                      ),
                                      
                                      
                                        #let's us add a button border undernealth the three container above
                                        # we will be using container
                                        #   Container(
                                        #       #this allows us to put one sidedborders
                                        #       border=border.only(bottom=border.BorderSide(0.35,'white')),
                                        #       #i want to bypass the overall padding so it can stretches from end-to-end
                                        #       #we do this by using marging parameters
                                        #       #margin=margin.only(left=18,right=18),
                                                      
                                        # ),
                                     
                                        # SideColumn(),
                                        
                                         Stack(controls=[
                                           
                                          SideColumn(),
                                          Container(
                                              # top=220,
                                              #left=20,
                                              opacity=0.9,
                                              # right=20,
                                              # bottom=100,
                                              content=gj,),
                                            ])
                                        
                                        #moving on,let see if we can create the numbers to the left side
                                        #let run a mini test and see some of the column aspect
                                        #perhaps if we put another inner column we will be able to manipulate it parameters with ease with disturbing the outer parameters
                                        
                                  ]
                              )
                          )
                          
                            
                    
                  ]),   
                ),
      
                



            ])  
      
    ])



    def create_container(image_path):
        return Container(
            content=Image(
                src=image_path,
                fit=ImageFit.COVER  # Ensures the image covers the container
            ),
            width=100,
            height=100,
            bgcolor= '#5525c9',#'#1e1e1e',
            border_radius=50,
            alignment=alignment.center
        )
        
    image_paths = [
        'images/2.png',
        'icons/apple.png',
        'icons/facebook.png',
        'icons/google.png',
        'icons/apple.png',
        'icons/facebook.png',
        'icons/google.png',
        'icons/apple.png',
        'icons/facebook.png',
        'icons/google.png',
        'icons/apple.png',
        'icons/facebook.png',
        # Add more image paths as needed
    ]

    page2C1 =[create_container(image_path) for image_path in image_paths]
    
    def scroll_containers():
        while True:
            for _ in range(150):  # Adjust this value to match the width of your containers
                for container in page2C1:
                    container.left = container.left - 1 if container.left > -150 else 1050
                container_row.update()
                time.sleep(0.01)



    page2 = Row(page2C1, scroll=ScrollMode.ALWAYS,spacing=40)
    
    def page3_hover(e):
      if e.data == "true":
        e.control.bgcolor = '#5525c9'
        e.control.update()
        self.pg.update()
      else:
        e.control.bgcolor = colors.WHITE
        e.control.update()
        self.pg.update()
     
     
    
    page3_c12 = Column(spacing=25,controls=[
      
                      Row(alignment='center',controls=[
                              ft.Container(
                              content=ft.Icon(name=icons.HOME, color='white', size=50),
                              width=100,
                              height=100,
                              bgcolor='#f5c000',
                              border_radius=50,
                              alignment=ft.alignment.center
                          ),
                      ]),
                      
                      Row(alignment='center',controls=[Container(margin=margin.only(top=25),
                        content=Row(controls=[
                                  Text(
                                      spans=[
                                          TextSpan(
                                              "Manage Team Collab",
                                              TextStyle(
                                                  size=35,
                                                  weight=FontWeight.BOLD,
                                                  font_family='Poppins regular',
                                                  foreground=Paint(
                                                      gradient=PaintLinearGradient(
                                                          (0, 20), (150, 20), [colors.BLACK, colors.BLACK]
                                                      )
                                                  ),
                                              ),
                                          ),
                                      ],
                                  ),
                        
                                  ]
                                    
                        ))]),
                      
                      
                       Row(alignment='center',controls=[Container(width=400,
                        content=Column(controls=[
                                  Text( 'Task tracking, customer support help desk and workflow management all wrapped up into one simple issue tracker your team and customers will love.'
                                        ,font_family='poppins regular'
                                        ,size=18,color=colors.BLACK,weight=FontWeight.W_100,
                                    ),
                                  ]
                                    
                        ))]),
                      
                      
                       Row(alignment='center',controls=[Container(
                        content=Row(controls=[
                                  Text(
                                      spans=[
                                          TextSpan(
                                              "Contact Us",
                                              TextStyle(
                                                  size=25,
                                                  weight=FontWeight.BOLD,
                                                  font_family='Poppins regular',
                                                  foreground=Paint(
                                                      gradient=PaintLinearGradient(
                                                          (0, 20), (150, 20), [colors.BLACK, colors.BLACK]
                                                      )
                                                  ),
                                              ),
                                          ),
                                      ],
                                  ),
                        
                                  ]
                                    
                        ))]),
                           
                    ])
    
    
       
    
    def create_circle_container(icon_name, header_text, detail_text):
        return ft.Container(
          
            content=ft.Column([page3_c12,
                
                # ft.Text(header_text, size=16, weight='bold', color='white'),
                # ft.Text(detail_text, size=12, color='white')
            ],
            alignment=ft.alignment.center),
            width=pgw/3,
            height=(pgh * 70)/100,
            on_hover=page3_hover,
            #margin=2,
            #bgcolor='#1e1e1e',
            #border_radius=10,
            padding=10,
            alignment=ft.alignment.center,
                border=Border(
                #left=BorderSide(width=aborder_width, color=colors.GREY),
                right=BorderSide(width=aborder_width, color=colors.GREY),
                #top=BorderSide(width=aborder_width, color=colors.GREY),
                bottom=BorderSide(width=aborder_width, color=colors.GREY),
            ),
        )
    
    # Create containers for each row
    page3_row_1 = [
        create_circle_container('home', 'Header 1', 'Detail 1'),
        create_circle_container('star', 'Header 2', 'Detail 2'),
        create_circle_container('settings', 'Header 3', 'Detail 3')
    ]

    page3_row_2 = [
        create_circle_container('search', 'Header 4', 'Detail 4'),
        create_circle_container('favorite', 'Header 5', 'Detail 5'),
        create_circle_container('info', 'Header 6', 'Detail 6')
    ]
    
    page3_c1 = Column(spacing=25,controls=[
      
      
                      Row(alignment='center',controls=[Container(margin=margin.only(top=45),
                        content=Row(controls=[
                                  Container(width=40,height=2,bgcolor='#5525c9',),
                                  Text( 'Why Choose Us'
                                        ,font_family='poppins regular'
                                        ,size=18,color=colors.WHITE,weight=FontWeight.W_100,
                                    ),
                                  Container(width=40,height=2,bgcolor='#5525c9',),
                                  ]
                                    
                        ))]),
                      Row(alignment='center',controls=[Container(width=500,content=
                           Text(
                                      spans=[
                                          TextSpan(
                                              "Having Everything You Need In One Software",
                                              TextStyle(
                                                  size=50,
                                                  weight=FontWeight.BOLD,
                                                  font_family='Poppins regular',
                                                  foreground=Paint(
                                                      gradient=PaintLinearGradient(
                                                          (0, 20), (150, 20), [colors.WHITE, colors.WHITE]
                                                      )
                                                  ),
                                              ),
                                          ),
                                      ],
                                  ),
                        
                        )]),
                      Row(alignment='center',controls=[Container(width=700,margin=margin.only(bottom=25),content=
                        Text( 'Our platform enables teams to collaborate and share information in real-time, with features like document editing, communication tools, and project management.'
                                ,font_family='poppins regular'
                                ,size=18,color=colors.WHITE,weight=FontWeight.W_100,
                            ),
              
                        )]),
                   
                   
                   
                    ])
    
    
    
    
    
    Row(alignment='center',controls=Container(bgcolor=colors.RED,width=500,height=50))
    
    row_1 = Row(page3_row_1, alignment=MainAxisAlignment.SPACE_AROUND)
    row_2 = Row(page3_row_2, alignment=MainAxisAlignment.SPACE_AROUND)

    
    page3 = Column([page3_c1,Column(spacing=0,controls=[row_1, row_2])], alignment=ft.MainAxisAlignment.CENTER, spacing=20)




    homepages = Column(
        spacing=10,
        # height=pgh,
        # width=pgw,
        scroll=ScrollMode.ALWAYS,
        controls=[
            Container(
                alignment=alignment.top_left,
                bgcolor='#000000',
                height=pgh + (pgh *30)/100,
                key="A",
                content=Column(
                  alignment='center',
                  controls=[
                    #ft.Text("Section B"),
                    page1,
                  
                  ]),
                
            ),
            Divider(height=9, thickness=3),
            Container(
                content=page2,
                alignment=alignment.top_left,
                #bgcolor=colors.GREEN_200,
                margin=margin.only(top=25),
                height=(pgh * 15)/100,
                key="B",
            ),
            Divider(height=9, thickness=3),
            Container(
                content=page3,
                alignment=alignment.top_left,
                #bgcolor=colors.BLUE_200,
                height=pgh + (pgh * 90)/100,
                key="C",
            ),
            Container(
                Text("Section D"),
                alignment=alignment.top_left,
                bgcolor=colors.PINK_200,
                height=pgh,
                key="D",
            ),
        ],
    )


      
    
  
    self.pg.on_resize = page_resize
    
    
    def bmc(e):
      print('yes')
      e.bgcolor = '#f5c000',
      e.control.update()
      self.pg.update()
    
    
       
    
    def createoption(mylist,bigmenucard):
      
      bigmenucard.controls.clear()
      for i,opt in enumerate(mylist):
      
        if 'A1' in opt :
          a1,ropt = opt.split('-')
          bigmenucard.controls.append(
            TextButton(
                            # "Get Started",
                              content=Text(
                                  ropt,
                                  size=ttsize3,  # Set the desired text size
                                  color=colors.BLACK,
                              ),
                              
                            ),
            )
          
        else:
          bigmenucard.controls.append(
                          Container(
                            on_click=lambda e: print('yes it worked!'),
                            
                            content=TextButton(
                              
                              on_click= lambda e: print('yeah!'),
                            # "Get Started",
                              
                              content=Text(
                                  opt,
                                  size=ttsize1,  # Set the desired text size
                                  color=colors.WHITE,
                              ),
                              style=ButtonStyle(
                                  # color= '#5525c9',
                                    bgcolor = '#5525c9',
                                    overlay_color= '#f5c000',
                                    shape=RoundedRectangleBorder(radius=10),
                                    color={
                                        MaterialState.HOVERED: '#f5c000',
                                        MaterialState.FOCUSED: colors.BLACK,
                                        MaterialState.DEFAULT: colors.WHITE,
                                    },
                                    ),
                            ))
            )
          
      return bigmenucard
      
    aft1 = Row(spacing=0,controls=[
      Text( 'Home',size=ttsize2,color=colors.WHITE,weight=FontWeight.W_200,),
      Icon(icons.KEYBOARD_ARROW_DOWN,color=colors.WHITE, size=25),  
    ])  
    
    aft2 = Row(spacing=0,controls=[
      Text( 'Pages',size=ttsize2,color=colors.WHITE,weight=FontWeight.W_200,),
      Icon(icons.KEYBOARD_ARROW_DOWN,color=colors.WHITE, size=25),  
    ]) 
    
    homekey = Row()
    pagekey = Row()
    
    hkhome =  Container(
                  #bgcolor=colors.RED,
                  content=Column(controls=[
                    
                    Container(
                      padding=20,
                      content=Row(alignment='spaceBetween',
                        
                        controls=[
                          Column(spacing=5,
                            controls=[
                            createoption(smallcardoption1,smallmenucard1),
                          ],),
                      ]),
                      height= (pgh *20) / 100,
                      width=(pgw *15) / 100,
                      #opacity = 0.9,
                      border_radius=25,
                      #bgcolor = '#5525c9',#'#20f4f4f4',
                      blur = Blur(10,10,BlurTileMode.REPEATED),
                      shadow = BoxShadow(
                          1,
                          15,
                          colors.BLUE_GREY_300,
                          Offset(2,2),
                          ShadowBlurStyle.OUTER,
                      ),
                    
                    ),
                  ]),
                  
                  margin=margin.only(left=(pgw *30) / 100, ),
                  height= (pgh *20) / 100,
                  width=(pgw *12) / 100,
                  #bgcolor = '#100036',
                  border_radius=25,
                  
                )
    
    
    
    hkpage =  Container(
                  #bgcolor=colors.RED,
                  
                  content=Column(
                    
                    alignment='center',
                    controls=[
                    
                    Container(
                      padding=20,
                      content=Row(alignment='spaceBetween',
                        
                        controls=[
                          Column(spacing=5,
                            controls=[
                            createoption(bigcardoption1,bigmenucard1),
                          ],),
                          Column(spacing=5,
                            controls=[
                            createoption(bigcardoption2,bigmenucard2),
                          ],),
                          Column(spacing=5,
                            controls=[
                            createoption(bigcardoption3,bigmenucard3),
                          ],),
                      ]),
                      height= (pgh *40) / 100,
                      width=(pgw *35) / 100,
                      #opacity = 0.9,
                      border_radius=25,
                     # bgcolor = '#5525c9',#'#20f4f4f4',
                      blur = Blur(10,10,BlurTileMode.REPEATED),
                      shadow = BoxShadow(
                          1,
                          15,
                          colors.BLUE_GREY_300,
                          Offset(2,2),
                          ShadowBlurStyle.OUTER,
                      ),
                     # margin=margin.only(left=(pgw *40) / 100),
                    
                    ),
                  ]),
                  
                  margin=margin.only(left=(pgw *45) / 100),
                  height= (pgh *40) / 100,
                  width=(pgw *35) / 100,
                 # bgcolor = '#100036',
                  border_radius=25,
                 
                  
                )

  
    def home_hover(e,hkvalue):
      global home_click_st
      if e.data == "true" and home_click_st == True:
        #e.control.bgcolor = "blue"  
        if pagekey.controls:
          pass
          
        else:
          pagekey.controls.append(hkvalue)
            
      elif e.data == "false" and home_click_st == True:
        #e.control.bgcolor = "blue"  
        if pagekey.controls:
          pass
 
        else:
          pagekey.controls.append(hkvalue)
        
      elif e.data == "true" and home_click_st == False:
        #e.control.bgcolor = "blue"  
        if pagekey.controls:
          pass
          
        else:
          pagekey.controls.append(hkvalue)
        
      elif e.data == "false" and home_click_st == False:
        #e.control.bgcolor = "white"
        pagekey.controls.pop()
            
      e.control.update()
      self.pg.update() 
    
     
    def home_click(e,hkvalue,aft):
      global home_click_st
      if home_click_st:
        home_click_st = False
        aft.controls[1].name = icons.KEYBOARD_ARROW_DOWN 
      elif home_click_st == False:  
        home_click_st = True
        aft.controls[1].name = icons.KEYBOARD_ARROW_UP 
        
      e.control.update()
      self.pg.update()
      
     
    
    self.appbar = Container(
      
        bgcolor='#121212',
        #margin=0,
        #width= pgw,
        height = (pgh *10)/100,
        #expand=True,
        opacity=0.8,
        content=Column([
                Row(alignment='spaceBetween',
                    controls=[         
                      Container(
                        on_click=lambda e: clogo(e),         
                        # content=Image(
                        #   src="images/logosaastech.png",
                        #   height=logosize,
                        #   fit=ImageFit.FILL,
                        # ),
                        content=Text(
                                      spans=[
                                          TextSpan(
                                              "CELEB",
                                              TextStyle(
                                                  size=40,
                                                  weight=FontWeight.BOLD,
                                                  font_family='Poppins regular',
                                                  foreground=Paint(
                                                      gradient=PaintLinearGradient(
                                                          (0, 20), (150, 20), [colors.WHITE, colors.WHITE]
                                                      )
                                                  ),
                                              ),
                                          ),
                                      ],
                                  ),
                      ),
                      Row(
                              spacing=10,
                              controls=[
                                Row(
                                  controls=[                    
                                    Container(
                                      on_click= lambda e: home_click(e,hkhome,aft1),
                                      on_hover=lambda e: home_hover(e,hkhome),
                                      content=Column(
                                        controls=[
                                        
                                        Row(spacing=0,
                                            controls=[    
                                            aft1,
                                        ])
                                      ] )
                                      ),
                              
                                      ]
                                  
                                      ),
                            
                            Text('About',size=ttsize2,color=colors.WHITE,weight=FontWeight.W_200),
                            Text('Blog',size=ttsize2,color=colors.WHITE,weight=FontWeight.W_200),
                            Row(
                                  controls=[                    
                                    Container(
                                      
                                      on_click=lambda e: home_click(e,hkpage,aft2),
                                      on_hover=lambda e: home_hover(e,hkpage),
                                      content=Column(
                                        controls=[
                                        
                                        Row(spacing=0,
                                            controls=[    
                                            aft2 ,
                                        ])
                                      ] )
                                      ),
                              
                                      ]
                                      ),
                            Text('Contact',size=ttsize2,color=colors.WHITE,weight=FontWeight.W_200),
                            
                          ]
                        ),
                      
                      Row(
                        alignment='spaceBetween',
                        spacing=lgs,
                        controls=[   
                            Row(
                          spacing=15,
                          controls=[
                          
                            Stack(
                              
                              [
                                  Icon(icons.SHOPPING_CART,size=ttsize5,color=colors.WHITE),
                                  Container(
                                      content=CircleAvatar(content=Text("0"),bgcolor=colors.AMBER, radius=(ttsize5 * 33.3)/ 100),
                                      alignment=alignment.top_right,
                                  ),
                              ],
                              width=40,
                              height=40,
                          ),
                            
                            Text('Sign In',size=ttsize2,color=colors.WHITE,weight=FontWeight.W_200),
                            FilledButton(
                              # "Get Started",
                                content=Text(
                                    "Get Started",
                                    size=ttsize3,  # Set the desired text size
                                ),
                                width=160,  # Set the desired width
                                height=60,  # Set the desired height
                                style=ButtonStyle(
                                  # color= '#5525c9',
                                    bgcolor = '#f5c000',
                                    overlay_color= colors.WHITE,
                                    shape=RoundedRectangleBorder(radius=10),
                                    color={
                                        MaterialState.HOVERED: colors.BLACK,
                                        MaterialState.FOCUSED: colors.BLACK,
                                        MaterialState.DEFAULT: colors.BLACK,
                                    },
                                    
                        
                                    ),
                              
                            ),    
                            
                          ]
                        ),
                        
                        ])
                      
                      
                    ]
                    
                    ),
                
                Row(
            #spacing=0,
            
            controls=[
              
             Container(
               #alignment='center',
               content=homekey,
             ),
             Container(
               #alignment='center',
               content=pagekey,
             )
             #pagekey,
            
          ])
        
        ])
      )
                 
    self.content = Stack(  
        alignment=alignment.center,    
        height= self.pg.height , #base_height,
        width= self.pg.width,
        
        
        controls=[   
            homepages,
            self.appbar,
        ]
      )
    
    self.pg.add(self.content,)
    
    #typ()
    
     # Run the scrolling in a separate thread
    # scroll_thread = Thread(target=scroll_containers)
    # scroll_thread.start()
        