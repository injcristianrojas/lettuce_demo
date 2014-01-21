from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
  # Este funciona con http://dcallagh.fedorapeople.org/phantomjs/phantomjs-1.9.0-1.fc20.x86_64.rpm en Fedora
  world.browser = webdriver.PhantomJS()
  # Si no funciona, usar Firefox
  #world.browser = webdriver.Firefox()