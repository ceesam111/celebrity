from flet import *
from utils.extras import *
bgcolor1='#f5c000'
bgcolor2='#5525c9'
bgcolor3='#121212'
base_height2 = 400


class LoginPage(Container):
  def __init__(self,switch_page,name,email,dp,pg):
    super().__init__()
    self.name = name
    self.email = email
    self.dp_url = dp
    self.offset = transform.Offset(0,0,)
    self.switch_page = switch_page
    self.expand = True
    self.view_hide_text = Text(
      value='View',
      color=base_color,
      font_family='poppins medium',
      
    )

    self.pwd_input = Container(
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

    self.error = Row(
      controls=[
        Image(
          src='assets/icons/danger.png',
          # scale=0.8,

        ),
        Text(
          value='Please enter the correct password to login',
          color='red',
          font_family='poppins regular'

        )
      ]
    )
    
    self.login_box = Column(
      controls=[
        Row(
          controls=[
            Container(
              height=50,width=50,bgcolor='white',border_radius=25,
              image_fit=ImageFit.COVER,image_src=img_src
            ),
            Column(
              spacing=0,
              controls=[
                Text(
                  value=self.name,
                  font_family='Poppins Semibold',
                  size=14,
                ),
                Text(
                  value=self.email,
                  font_family='Poppins light',
                  size=14,
                ),
              ]
            )
          ]
        ),
        
        Container(height=2),
        
        self.pwd_input,
        
        Container(height=1),

        # self.error,
        
        Container(height=1),

        Container(
          data = 'login_clicked',
          on_click= self.switch_page,
          height=btn_height,
          width=btn_width,
          bgcolor=base_green,
          border_radius=10,
          alignment=alignment.center,
          content=Text(
            value='Continue',
            font_family='Poppins Medium',
            size=16,

          )
        ),
        Container(height=5),


        
        Container(
          content=Text(
            value="Forgot your password?",
            size=14,
            font_family='poppins medium',
            color=base_green
          ),
        ),
        
        Container(height=5),

      ]
    )


    
    
    self.main_content = Column(
      #scroll=ScrollMode.ALWAYS,
      # expand = True,
      controls=[
        
        Container(
                    padding=20,
                    # height=550,
                    bgcolor='#cc2d2b2c',
                    border_radius=10,
                    content=self.login_box,
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
                      value='Login',
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

    y = self.error in self.login_box.controls
    if y == True:
      self.login_box.controls.remove(self.error)
      self.pwd_input.bgcolor = 'white'
      self.pwd_input.border = None
      self.pwd_input.update()
      self.login_box.update()

      # pass
  def view_hide_password(self,e):
    det = self.pwd_input.content.password
    if det == True:
      self.pwd_input.content.password = False
      self.view_hide_text.value = 'Hide'
    else:
      self.view_hide_text.value = 'View'
      self.pwd_input.content.password = True
    self.pwd_input.content.update()
    self.view_hide_text.update()




