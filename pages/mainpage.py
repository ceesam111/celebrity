from flet import *
from utils.extras import *
bgcolor1='#f5c000'
bgcolor2='#5525c9'
bgcolor3='#121212'
base_height2 = 400


class MainPage2(Container):
  def __init__(self,switch_page,pg):

    super().__init__()
    self.offset = transform.Offset(0,0,)
    self.switch_page = switch_page
    self.pg = pg
    
    
    
    # pgh = pg.window_height
    # pgw = pg.window_width
    
    # pghh = pg.height
    # pgww = pg.width
    
    
    # base_height2 = (pgh * 58) / 100 if pgh != 0.0 else (pghh * 58) / 100
    # print('start' + ' ' + str(base_height2) + ' ' + str(pghh))
    # base_width2 = (pgw * 35) / 100
    # print('start' + ' ' + str(base_width2))
    
    
     
  
  
  
    self.error = Row(
      controls=[
        Image(
          src='icons/danger.png',
          # scale=0.8,

        ),
        Text(
          value='Please check your email address.',
          color='red',
          font_family='poppins regular'

        )
      ]
    )
    
    
    print(pg.width)
    
    #self.expand = True
    self.email_input = Container(
      # width =  300 if pg.width <= 385 else btn_width,
      height=btn_height,
      bgcolor='white',
      border_radius=10,
      content=TextField(
        on_focus=self.field_in_focus,
        hint_text='Email',
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
    )

    self.main_content = Column(
      #scroll=ScrollMode.ALWAYS,
      # expand = True,
      controls=[
        self.email_input,
        Container(height=0),
        Container(
          on_click=self.switch_page,
          data = 'process_login',
          height=btn_height,
          # width =  300 if pg.width <= 385 else btn_width,
          bgcolor=base_green,
          border_radius=10,
          alignment=alignment.center,
          content=Text(
            value='Continue',
            font_family='Poppins Medium',
            size=18,
          )
        ),
        
        Row(
          alignment='center',
          controls=[
            Text(
              value='or',
              size=16,
              font_family='Poppins regular',
            )
          ]
        ),
        
        Container(
          height=btn_height,
          width=btn_width,
          bgcolor=light_green,
          border_radius=10,
          alignment=alignment.center,
          padding=10,
          content=Row(
            
            controls=[
              Image(
                src='icons/facebook.png',
                scale=0.7
              ),
              Text(
                value='Continue with Facebook',
                font_family='Poppins semibold',
                size=18,
                color=base_color,
                


              ),
            ]
          )
        ),

        Container(height=0),

        Container(
          height=btn_height,
          width=btn_width,
          bgcolor=light_green,
          border_radius=10,
          alignment=alignment.center,
          padding=10,
          content=Row(
            controls=[
              Image(
                src='icons/google.png',
                scale=0.7
              ),
              Text(
                value='Continue with Google',
                font_family='Poppins semibold',
                size=18,
                color=base_color,
                #scale = 0.9,
             


              ),
            ]
          )
        ),
        
        Container(height=0),
        
       ResponsiveRow([
         Container(
          height=btn_height,
          width=50,
          # max_width=300,
          bgcolor=light_green,
          border_radius=10,
          alignment=alignment.center,
          padding=10,
          col={"sm": 12},
          content=Row(
            controls=[
              Image(
                src='icons/apple.png',
                scale=0.7
              ),
              Text(
                value='Continue with Apple',
                font_family='Poppins semibold',
                size=18,
                color=base_color,


              ),
            ]
          )

        ),
          ]) ,
        Container(height=20),

        Text(
          value="Forgot your password?",
          color=base_green,
          size=16,
          font_family='Poppins Regular',
        ),
        
        Container(height=20),

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
        content=Column(controls=[
          
          Stack(controls=[
          
          #  Container(
          #           # expand=True,
          #           # bgcolor=bgcolo,
          #           padding=20,
          #           data = 'light',
          #           on_click = self.switch_page,
          #           content=Row(controls=[Icon(
          #             icons.ARROW_BACK_IOS_OUTLINED,
          #             size=28
          #           )]),
          #         ), 
           
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
                    data = 'light',
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
                      value='Hi!',
                      font_family='Poppins Bold',
                      size=30,
                    ),
                  ),
                  Container(height=2),
                  Container(
                    
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
                
                   ),
           ] )

            )
           
          ]
        )]),
         
        
          
          ])
        
        ])
      )
    
  def field_in_focus(self,e):

    y = self.error in self.main_content.controls
    if y == True:
      self.main_content.controls.remove(self.error)

      self.email_input.bgcolor = 'white'
      self.email_input.border = None
      self.main_content.update()