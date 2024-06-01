from flet import *
from utils.extras import *
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
      # hkpage.margin = margin.only(left=(pgw *35) / 100)
      # hkhome.margin = margin.only(left=(pgw *25) / 100)
      # homepages.height = pgh
      # homepages.width = pgw
      # #print('ti' + str((pgw *30) / 100))
      
      # self.content.update()
      
      self.pg.update()
   
      
   
   
      print((ttsize5,ttsize2,ttsize1,logosize,lgs))
    
      base_height2 = (pgh * 58) / 100 
      print('start2' + ' ' + str(base_height2) )
      base_width2 = (pgw * 35) / 100
      print('start2' + ' ' + str(base_width2))
    

    
    
    page1 = Column(
      
      controls=[
        
            Row(
              #spacing=5,
              alignment='spaceBetween',
              controls=[
                Container(
                  width = (pgw * 42) / 100,
                  height = (pgh * 80) / 100 ,
                  #bgcolor = colors.AMBER,
                  content=Column(#alignment='spaceBetween',
                                 spacing='5',
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
                                                                  (0, 20), (150, 20), [colors.BLACK, colors.BLACK]
                                                              )
                                                          ),
                                                      ),
                                                  ),
                                              ],
                                          )
                                      
                                    ),
                                    
                                    Container(
                                      content=Text( 'Learn where your audience struggle as they navigate your digital business. Pair this understanding of the individual experience with powerful quantitative insights to inform your digital decisions.'
                                                   ,font_family='poppins regular'
                                         ,size=ttsize1,color=colors.BLACK,weight=FontWeight.W_100,
                                    )
                                    ),
                                ]),   
                ),
                Container(
                  width = (pgw * 55) / 100,
                  height = (pgh * 100) / 100 ,
                  #bgcolor = colors.BLUE,
                  content=Column([
                    
                  ]),   
                ),
      
            ])  
      
    ])

    homepages = Column(
        spacing=10,
        height=pgh,
        width=pgw,
        scroll=ScrollMode.ALWAYS,
        controls=[
            Container(
                alignment=alignment.top_left,
                #bgcolor=ft.colors.YELLOW_200,
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
                Text("Section B"),
                alignment=alignment.top_left,
                bgcolor=colors.GREEN_200,
                height=pgh,
                key="B",
            ),
            Container(
                Text("Section C"),
                alignment=alignment.top_left,
                bgcolor=colors.BLUE_200,
                height=pgh,
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
                            on_hover=lambda e: bmc(e),
                            content=TextButton(
                            # "Get Started",
                              
                              content=Text(
                                  opt,
                                  size=ttsize1,  # Set the desired text size
                                  #color=colors.WHITE,
                              ),
                              style=ButtonStyle(
                                  # color= '#5525c9',
                                    bgcolor = '#5525c9',
                                    #overlay_color= '#f5c000',
                                    shape=RoundedRectangleBorder(radius=10),
                                    color={
                                        MaterialState.HOVERED: '#f5c000',
                                        #MaterialState.FOCUSED: colors.BLACK,
                                        MaterialState.DEFAULT: colors.WHITE,
                                    },
                                    ),
                            ))
            )
          
      return bigmenucard
      
    aft1 = Row(spacing=0,controls=[
      Text( 'Home',size=ttsize2,color=colors.BLACK,weight=FontWeight.W_200,),
      Icon(icons.KEYBOARD_ARROW_DOWN,color=colors.BLACK, size=25),  
    ])  
    
    aft2 = Row(spacing=0,controls=[
      Text( 'Pages',size=ttsize2,color=colors.BLACK,weight=FontWeight.W_200,),
      Icon(icons.KEYBOARD_ARROW_DOWN,color=colors.BLACK, size=25),  
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
                      opacity = 0.9,
                      border_radius=25,
                      bgcolor = '#5525c9',#'#20f4f4f4',
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
                  bgcolor = '#100036',
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
      
     
    print(lgs)
    
    self.appbar = Container(
      
        bgcolor = colors.WHITE,
        width= pgw,
        height = (pgh *10)/100,
        #opacity=0.5,
        content=Column([
          
                Row(alignment='spaceBetween',
                    
                    controls=[
                      
                      Container(
                        on_click=lambda e: clogo(e),
                        
                        content=Image(
                          src="images/logosaastech.png",
                          #width=200,
                          height=logosize,
                          fit=ImageFit.FILL,
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
                            
                            Text('About',size=ttsize2,color=colors.BLACK,weight=FontWeight.W_200),
                            Text('Blog',size=ttsize2,color=colors.BLACK,weight=FontWeight.W_200),
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
                            Text('Contact',size=ttsize2,color=colors.BLACK,weight=FontWeight.W_200),
                            
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
                                  # ft.CircleAvatar(
                                  #     foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
                                  # ),
                                  
                                  Icon(icons.SHOPPING_CART,size=ttsize5,color=colors.BLACK),
                                  Container(
                                      content=CircleAvatar(content=Text("0"),bgcolor=colors.AMBER, radius=(ttsize5 * 33.3)/ 100),
                                      alignment=alignment.top_right,
                                  ),
                              ],
                              width=40,
                              height=40,
                          ),
                            
                            Text('Sign In',size=ttsize2,color=colors.BLACK,weight=FontWeight.W_200),
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
                                    bgcolor = '#5525c9',
                                    overlay_color= '#f5c000',
                                    shape=RoundedRectangleBorder(radius=10),
                                    color={
                                        MaterialState.HOVERED: colors.BLACK,
                                        MaterialState.FOCUSED: colors.BLACK,
                                        MaterialState.DEFAULT: colors.WHITE,
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
            
              # Container(
              #   bgcolor=colors.RED,
              #   height=150,
              #   width=300,
              #   border_radius=25,
              #   margin=margin.only(left=(pgw *30) / 100),
              # ),
              
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
        #padding=padding.symmetric(
        #horizontal=8,vertical=20),
       # margin = 0,
        alignment=alignment.center,
        
         
        height= self.pg.height , #base_height,
        width= self.pg.width,
        #margin = 0,
        #bgcolor=base_color,
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        #expand=True,
       # border_radius=br,
        controls=[
          
            homepages,
            self.appbar,
          
        ]
      )
        
      
    
    
    
  def field_in_focus(self,e):

    y = self.error in self.main_content.controls
    if y == True:
      self.main_content.controls.remove(self.error)

      self.email_input.bgcolor = 'white'
      self.email_input.border = None
      self.main_content.update()