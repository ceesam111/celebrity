from flet import *
import pickle
import os
from utils.extras import *
from pages.mainpage import MainPage2
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.dashboard import DashboardPage
from pages.index import Index2
from service.auth import get_user,authenticate, verify_token, register_user, is_valid_email,cUser
import asyncio
#from http.server import HTTPServer, BaseHTTPRequestHandler
#import logging, ngrok


async def save_token(token):
  try:
    with open("token.pkl", "wb") as f:
      pickle.dump(token, f)
    return 'Saved'
  except:
    return None 



async def load_token():
  try:
    with open("token.pkl", "rb") as f:
      stored_token = pickle.load(f)
    return stored_token
  except:
    return None



class WindowDrag(UserControl):
  def __init__(self):
    super().__init__()
    # self.color = color
  def build(self):
    return True #Container(content=WindowDragArea(height=10,content=Container(bgcolor='white')))


class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    
    # pg.horizontal_alignment = "center"
    # pg.vertical_alignment = "center"

   # pg.window_title_bar_hidden = False
    #pg.window_frameless = False
    #pg.window_title_bar_buttons_hidden = False
    
    pg.vertical_alignment = MainAxisAlignment.CENTER
    pg.horizontal_alignment = CrossAxisAlignment.CENTER
    #pg.bgcolor= base_color
    #pg.bgcolor='#000000',
    pg.bgcolor = colors.BLACK
    pg.window_resizable = True
    pg.expand = True

    pg.spacing = 0,
    pg.update(),
    # pg.window_left = 400
    # pg.window_top = 400

    # pg.bgcolor = colors.TRANSPARENT
    #pg.window_bgcolor = '#000000',
    pg.fonts = {
    "SF Pro Bold":"fonts/SFProText-Bold.ttf",
    "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
    "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
    "SF Pro Light":"fonts/SFProText-Light.ttf",
    "SF Pro Medium":"fonts/SFProText-Medium.ttf",
    "SF Pro Regular":"fonts/SFProText-Regular.ttf",
    "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
    "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
    
    
    "Poppins ThinItalic":"fonts/poppins/Poppins-ThinItalic.ttf",
    "Poppins Thin":"fonts/poppins/Poppins-Thin.ttf",
    "Poppins Semibold":"fonts/poppins/Poppins-Semibold.ttf",
    "Poppins SemiboldItalic":"fonts/poppins/Poppins-SemiboldItalic.ttf",
    "Poppins Regular":"fonts/poppins/Poppins-Regular.ttf",
    "Poppins MediumItalic":"fonts/poppins/Poppins-MediumItalic.ttf",
    "Poppins Medium":"fonts/poppins/Poppins-Medium.ttf",
    "Poppins LightItalic":"fonts/poppins/Poppins-LightItalic.ttf",
    "Poppins Light":"fonts/poppins/Poppins-Light.ttf",
    "Poppins Italic":"fonts/poppins/Poppins-Italic.ttf",
    "Poppins ExtraLightItalic":"fonts/poppins/Poppins-ExtraLightItalic.ttf",
    "Poppins ExtraLight":"fonts/poppins/Poppins-ExtraLight.ttf",
    "Poppins ExtraBold":"fonts/poppins/Poppins-ExtraBold.ttf",
    "Poppins ExtraBoldItalic":"fonts/poppins/Poppins-ExtraBoldItalic.ttf",
    "Poppins BoldItalic":"fonts/poppins/Poppins-BoldItalic.ttf",
    "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
    "Poppins BlackItalic":"fonts/poppins/Poppins-BlackItalic.ttf",
    "Poppins Black":"fonts/poppins/Poppins-Black.ttf",
  }
    
    # def page_resize(e):
    #   print("New page size:", pg.window_width, pg.window_height)

    # pg.on_resize = page_resize 
    
    # if pg.platform == PagePlatform.MACOS:
    #     print(pg.window_width)
    #     print(pg.window_height)
        
    # elif pg.platform == PagePlatform.ANDROID:
    #     print(pg.window_width)
    #     print(pg.window_height)
        
    # elif pg.platform == PagePlatform.IOS:
    #     print(pg.window_width)
    #     print(pg.window_height)
        
    # elif pg.platform == PagePlatform.WINDOWS:
    #     print(pg.window_width)
    #     print(pg.window_height)
    #     print(pg.window_max_width)
    #     print(pg.window_max_height)
        
    #     print('this is a window screen')
        
    #     # width=400,
    #     # height=850,
    #     #pg.padding = 0,
    #     #pg.window_left = 0,
    #     # pg.horizontal_alignment = "center"
    #     # pg.vertical_alignment = "center"
    #     pg.window_width = pg.window_width - 10
    #     pg.window_height = pg.window_height 

        
    # elif pg.platform == PagePlatform.LINUX:
    #     print(pg.window_width)
    #     print(pg.window_height)
    

    auth = asyncio.run(verify_token(asyncio.run(load_token())))
    self.pg  = pg
    #self.pg.spacing = 0
    self.delay = 0.1
    self.anim = animation.Animation(300,AnimationCurve.EASE_IN_OUT_CUBIC)

    self.main_page = MainPage2(self.switch_page,self.pg)
    
    # self.index_page2 = Index2(self.switch_page,self.pg)
    
    self.screen_views = Stack(
        expand=True,
        controls=[
          Index2(self.switch_page,self.pg) if not auth else DashboardPage(self.switch_page, auth["email"]),
        ]
      )

    self.init_helper()

  def switch_page(self,e):
    print(e.control.data)
    if e.control.data == 'register':
      name = self.signup_page.name_box.value
      password = self.signup_page.password_box.content.value
      email = self.main_page.email_input.content.value
      
      donecUser = cUser(name=name,password=password,email=email)
   
      user = register_user(name, email, password)
      self.screen_views.controls.clear()
      self.screen_views.controls.append(DashboardPage(self.switch_page,email,))
      self.screen_views.update()
      # return


    elif e.control.data == 'process_login':
      email = self.main_page.email_input.content.value
      if is_valid_email(email):
        user = get_user(email)
        if user:
          id = user[0]
          self._name = user[1]
          self._email = user[2]
          self.screen_views.controls.clear()
          self.login_page = LoginPage(self.switch_page,name=self._name,email=self._email,dp='',pg=self.pg)
          # self.login_page.content.on_focus = self.hide_error
          self.screen_views.controls.append(self.login_page)
          self.screen_views.update()
        else:
          self.screen_views.controls.clear()  
          self.signup_page = SignupPage(self.switch_page,email,self.pg)
          self.screen_views.controls.append(self.signup_page)
          self.screen_views.update()
      else:
        self.main_page.email_input.bgcolor = input_error_bg
        self.main_page.email_input.border = border.all(width=2,color=input_error_outline)
        
        self.main_page.main_content.controls.insert(1,self.main_page.error)

        self.main_page.update()
        # self.main_page.email_input.update()
        
      
    elif e.control.data == 'main_page':
      print("get to main")
      self.screen_views.controls.clear()
      self.screen_views.controls.append(self.main_page)
      self.screen_views.update()
      self.pg.update()
      print("after main")
      
    elif e.control.data == 'light':
      print('yeah!')
      self.screen_views.controls.clear()
      self.screen_views.controls.append(Index2(self.switch_page,self.pg))
      self.screen_views.update()
      
    elif e.control.data == 'login_clicked':
      password = self.login_page.pwd_input.content.value
      email = self.login_page.email
      
      print(password,email)

      auth = authenticate(email,password)
      print(str(auth))
      if auth:
        asyncio.run(save_token(auth))
        self.screen_views.controls.clear()
        self.screen_views.controls.append(DashboardPage(self.switch_page,email))
        self.screen_views.update()

      else:
        self.login_page.login_box.controls.insert(4,self.login_page.error)  
        self.login_page.pwd_input.bgcolor = input_error_bg
        self.login_page.pwd_input.border=border.all(width=2, color=input_error_outline)
        self.login_page.pwd_input.update()
        self.login_page.login_box.update()

    elif e.control.data == 'logout':
      try:
        os.remove('token.pkl')  
      except Exception as e:
        print(e)
        pass
      self.screen_views.controls.clear()
      self.screen_views.controls.append(Index2(self.switch_page,self.pg))
      self.screen_views.update()

    


      

  def init_helper(self):
    self.pg.add(
      #WindowDrag(),
      self.screen_views 
    )

run = app(target=App,assets_dir='/assets', view=WEB_BROWSER,export_asgi_app=True)

#app(target=App,assets_dir='assets')#,export_asgi_app=True,)

#run = app(target=App,assets_dir='assets',export_asgi_app=True,)

# class HelloHandler(BaseHTTPRequestHandler):
#   def do_GET(self):
#       body = bytes("Hello", "utf-8")
#       self.protocol_version = "HTTP/1.1"
#       self.send_response(200)
#       self.send_header("Content-Length", len(body))
#       self.end_headers()
#       self.wfile.write(body)


# # logging.basicConfig(level=logging.INFO)
# # server = HTTPServer(("localhost", 0), HelloHandler)
# # ngrok.listen(server)
# # server.serve_forever()

# # Setup and start the HTTP server with ngrok
# server = HTTPServer(("localhost", 5000), HelloHandler)
# public_url = ngrok.connect(5000)
# print(f"Ngrok tunnel: {public_url}")

# try:
#     server.serve_forever()
# except KeyboardInterrupt:
#     server.server_close()
#     ngrok.disconnect(public_url)
#     print("Server stopped")
