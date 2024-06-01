from flet import *
from utils.extras import *


bgcolor1='#f5c000'
bgcolor2='#5525c9'
bgcolor3='#121212'
base_height2 = 400


class SignupPage(Container):
  def __init__(self,switch_page,email,pg):
    super().__init__()
    
    self.email = email
    self.offset = transform.Offset(0,0,)
    self.switch_page = switch_page
    self.pg = pg
    self.view_hide_text = Text(
      value='View',
      color=base_color,
      font_family='poppins medium',
      
    )
    
    # pgh = pg.window_height
    # pgw = pg.window_width
    
    # pghh = pg.height
    # pgww = pg.width
    
    
    # base_height2 = (pgh * 58) / 100 if pgh != 0.0 else (pghh * 58) / 100
    # print('start' + ' ' + str(base_height2) + ' ' + str(pghh))
    # base_width2 = (pgw * 35) / 100
    # print('start' + ' ' + str(base_width2))
    
    
     
  
  
  
    # self.expand = True
    self.password_box = Container(
      height=btn_height,
      bgcolor='white',
      border_radius=10,
      # padding=20,
      content=TextField(
        on_focus=self.password_field_in_focus,
        password=True,
        suffix=Container(
          on_click=self.view_hide_password,
          content=self.view_hide_text,                              
        ),
        hint_text='Password',
        hint_style=TextStyle(
          size=16,
          font_family='Poppins Regular',
          color=input_hint_color,
        ),
        text_style=TextStyle(
          size=16,
          font_family='Poppins Regular',
          color=input_hint_color,
        ),
        border=InputBorder.NONE,
        content_padding=content_padding,
        selection_color=base_green,
        cursor_color=base_color
      )
    )
    
    self.name_box = TextField(
      hint_text='Name',
      hint_style=TextStyle(
        size=16,
        font_family='Poppins Regular',
        color=input_hint_color,
      ),
      text_style=TextStyle(
        size=16,
        font_family='Poppins Regular',
        color=input_hint_color,
      ),
      border=InputBorder.NONE,
      content_padding=content_padding
    )

    self.error = Row(
      controls=[
        Image(
          src='assets/icons/danger.png',
          # scale=0.8,

        ),
        Text(
          value='Please check your email address.',
          color='red',
          font_family='poppins regular'

        )
      ]
    )
    
    
    
    self.main_content = Column(
      #scroll=ScrollMode.ALWAYS,
      # expand = True,
      controls=[
        
        Container(content=Column(
                          spacing=0,
                          controls=[
                            Text(
                              value=f'Looks like you don\'t have an account.\nLet\'s create a new account for',
                              size=14,
                              font_family='poppins light',
                              color='#ccffffff'
                            ),
                            Text(
                              value=self.email,
                              size=14,
                              font_family='poppins medium',
                              color='#ccffffff'
                            ),
                          ]
                        ),),
        
        Container(height=1),
        Container(
          height=btn_height,
          bgcolor='white',
          border_radius=10,
          # padding=20,
          content=self.name_box,
        ),
        Container(height=1),



        Container(
          height=btn_height,
          bgcolor='white',
          border_radius=10,
          # padding=20,
          content=self.password_box,
        ),
        Container(height=1),
        Container(
          content=Column(
            spacing=0,
            controls=[
              Text(
                value="By clicking 'Agree and Continue' below,",
                size=14,
                font_family='poppins light',
                color='#ccffffff'
              ),
              Column(
                spacing=0,
                controls=[
                  Text(
                    value="I agree to ",
                    size=14,
                    font_family='poppins light',
                    color='#ccffffff'
                  ),
                  Text(
                    value="Terms of Service and Privacy Policy",
                    size=14,
                    font_family='poppins medium',
                    color=base_green
                  ),
                ]
              )
            ]
          )
        ),

        
        Container(height=1),
        
        Container(
          data='register',
          on_click=self.switch_page,
          height=btn_height,
          width=btn_width,
          bgcolor=base_green,
          border_radius=10,
          alignment=alignment.center,
          content=Text(
            value='Agree and Continue',
            font_family='Poppins Medium',
            size=16,

          )
        ),
        Container(height=30),
        

       
                  

      ]
    )
    
    
    
    
    jform = Column( 
            controls=[self.main_content],
            height=400,
          #  width=base_width,
            scroll=ScrollMode.HIDDEN,
            #auto_scroll = True,
          
            
            )
    
    
    
    #jform.scroll_to(delta=50)

    
                  
    self.content = Container(
      
        # padding=padding.symmetric(
        # horizontal=8,vertical=20),
        
         
        # height= self.pg.height, #base_height,
        # width= self.pg.width,
        #margin = 0,
        
        bgcolor=base_color,
        margin = 0,
        alignment=alignment.center,
        
        # clip_behavior=ClipBehavior.ANTI_ALIAS,
        #expand=True,
        border_radius=br,
        content=Column(scroll=ScrollMode.HIDDEN,controls=[
          
          Stack(controls=[
       
           
           Row(controls=[
             
             Container(
                    # expand=True,
                    # bgcolor=bgcolo,
                    # padding=20,
                    data = 'light2',
                    on_click = self.switch_page,
                    # content=Row(controls=[Icon(
                    #   icons.ARROW_BACK_IOS_OUTLINED,
                    #   size=28
                    # )]),
                  ), 
      
             
           ]),
      
          
          
          Row(
          # expand=True,
          alignment='center',
          controls=[
            Stack(controls=[
            Container(
              height=base_height,
              width=base_width,
              alignment=alignment.center,
              left=10,
              top=-270,
              content=Image(
                src='images/2.png',
                scale=0.9,
              )
            ),
            
            
            Container(
              height=base_height,
              
              width= base_width,
              border_radius=br,
              # margin=margin.only(bottom=100),
              # left=400,
              # top=-40,
              # bgcolor='red'
              padding=padding.only(top=30,left=10,right=10,),
              content=Column(
                controls=[
                  
                  Container(
                    # expand=True,
                    # bgcolor=bgcolo,
                    # padding=20,
                    data = 'main_page',
                    on_click = self.switch_page,
                    # ink=True,
                    # ink_color=bgcolor1,
                    content=Row(controls=[Icon(
                      icons.ARROW_BACK_IOS_OUTLINED,
                      size=28
                    )]),
                  ), 
      
                  
                  Container(height=100),
                  Container(
                    margin=margin.only(left=20),
                    content=Text(
                      value='Sign up',
                      font_family='Poppins Bold',
                      size=30,
                    ),
                  ),
                  Container(height=2),
                  Column(scroll=ScrollMode.HIDDEN,controls=[Container(
                    
                    #clip_behavior=ClipBehavior.ANTI_ALIAS,
                    #expand=True,
                    # margin=20,
                    height=400,
                    # width= base_width,
                    width =  350 if pg.width <= 385 else base_width,
                    padding=20,
                    bgcolor='#cc2d2b2c',
                    border_radius=25,
                    content=jform,
                
                   )]),
           ] )

            )
           
          ]
        )]),
         
        
          
          ]),
        
        ])
      )
    
  def field_in_focus(self,e):

    y = self.error in self.main_content.controls
    if y == True:
      self.main_content.controls.remove(self.error)

      self.email_input.bgcolor = 'white'
      self.email_input.border = None
      self.main_content.update()
      
  def password_field_in_focus(self,e):
    pass

    # y = self.error in self.login_box.controls
    # if y == True:
    #   self.login_box.controls.remove(self.error)
    #   self.pwd_input.bgcolor = 'white'
    #   self.pwd_input.border = None
    #   self.pwd_input.update()
    #   self.login_box.update()

      # pass
  def view_hide_password(self,e):
    det = self.password_box.content.password
    if det == True:
      self.password_box.content.password = False
      self.view_hide_text.value = 'Hide'
    else:
      self.view_hide_text.value = 'View'
      self.password_box.content.password = True
    self.password_box.content.update()
    self.view_hide_text.update()



