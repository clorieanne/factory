from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from factory.factory_method import *
import os

@step(u'Given that I visited the domain "([^"]*)" with path "([^"]*)"')
def given_that_i_visited_the_domain_group1_with_path_group2(step, website, path):
  assert True

@step(u'When I run the program')
def when_i_run_the_program(step):
  os.system('python facade.py')

@step(u'Then the program was able to fetch the following:')
def then_the_program_was_able_to_fetch_the_following_group1(step):
  assert_equal(get_http('localhost', ''),['google.com,facebook.com'] )

@step(u'Given that I visited the domain "([^"]*)" and path "([^"]*)" in ftp')
def give_that_I_visited_the_domain_group1_and_path_group2_in_ftp(step, website, path):
  assert True

@step(u'Then the program was able to fetch the following in ftp:')
def then_the_program_was_able_to_fetch_the_following_in_ftp(step):
  
  assert_equal(get_ftp('ftp.freebsd.org', '/pub/FreeBSD/'), ['C'])