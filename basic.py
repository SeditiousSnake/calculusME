#!/usr/bin/env python

import operator
import math
import re
from datetime import datetime as date

'''Calculus Made Easy'''

'''
import re

def factor(p):
    analyzing = True
    factor_pattern = '(\(x(\+|\-|\/|\*)(\d+)\)\^(\d+))'
#                      ^        ^         ^        ^
#                      |1       |2        |3       |4
    exponents = []
    factors = []
    print 'analyzing polynomial...'
    while analyzing:
        try:
            expnt = re.search(factor_pattern, p).group(0)
            p = p.replace(expnt, '')
            expnt = expnt.replace('^', '**')
            exponents.append(expnt)
        except:
            try:
                fctr = re.search(factor_pattern.replace('\^(\d+)',''), p).group(0)
                factors.append(fctr)
                p = p.replace(fctr, '')
            except:
                analyzing = False
    print 'new p: ', p
    print 'exponents: ', exponents
    print 'factors: ', factors

factor('(x+5)^2(x+3)^3(x+2)')

class x:
    def __init__(self):
        pass
    
    def mul_behavior(self, p):
        try:
            if self.var is p.var:
                print '%s^2' % self.var
    
    def __mul__(self, p):
        self.mul_behavior(p)
    
    def __rmul__(self, p):
        self.mul_behavior(p)
        
x1 = x()
x2 = x()

x1 * x2

eq = '(x+5)(x+3)'
xs = {}

for x in range(len(re.findall('x', eq))):
    xs['x%s'%x]


Solution to x:
    -- get all instances of x
    -- add them to a unique key in a dict
        -- xs = {
            'x1': 'x',
            'x2': 'x',
            'x3': 'x'
        }
    -- assign each key
'''

cmds = ['limit', 'derivative', 'dataset']
dscmds = ['avgroc', 'instroc']

class calculusME:
    def __init__(self):
        self.cleanup(dset=True)
        self.rules()
        self.lim = None
        while True:
            cmd = raw_input('>')
            for k in re.findall('\-\-(\w+)', cmd):
                cmd = cmd.replace(" --"+k,'')
                self.opts[k] = True
            if cmd == 'help':
                print self.options()
            elif cmd == 'quit' or cmd == 'exit':
                break
            elif cmd == 'rules':
                self.rules()
            elif cmd in cmds:
                print getattr(self, cmd)()
            else:
                print 'no command %s' % cmd
    
    def rules(self):
        print(
"""Rules of CalculusME:
    -- use parentheses ie (2x+2)/(1x+1)
    -- use 'x' for variable
    -- if just 'x', put '1x'
    -- type 'help' for options
    -- type 'quit' to exit
    -- type 'rules' for this menu
    -- absolutely, positively NO SPACES!""")
    
    def options(self):
        return(
"""Options:
    -- limit
    -- derivative
    -- dataset""")
    
    def format_equation(self):
        '''format f(x) for exponents'''
        self.lim = self.lim.replace('^', '**')
        
    def substitute_x(self, eq, x):
        opx = '(\+|\-|\/|\*)x'
        while opx:
            try:
                '''find operator in front of x'''
                op = re.search(
                    opx, eq).group(1)
                '''increment x with operator'''
                eq = eq.replace(op+'x', x)
            except:
                opx = False
            
        opx = '(\+|\-|\/|\*)x'
        '''replace x multiples and increment it'''
        eq = eq.replace('x', '*'+x)
        return eq
    
    def dataset(self):
        if not self.dset or self.opts['new_dset'] == True:
            self.cleanup(dset=True)
            try:
                print 'enter your table data (ie 1994(enter)0708(enter)'
                self.kunit = raw_input('y unit>')
                self.vunit = raw_input('x unit>')
                while self.entered is False:
                    try:
                        key = float(raw_input('f(x)>'))
                        val = float(raw_input('x>'))
                    except ValueError:
                        return "f(x) and x cannot contain letters"
                    self.dset[key] = val
                    if raw_input('"n" to cont.>') != 'n':
                        self.entered = True
                    else:
                        pass
                print 'building dataset...'
                print 'dataset session started @ %s' % (
                    re.search('(.+)(\.\d+)', str(date.now().time())).group(1))
            except:
                return 'data set entered incorrectly'
            
        self.display_dataset()
        self.dataset_opts()
        self.dataset_menu()
        return 'dataset session exit @ %s' % (
            re.search('(.+)(\.\d+)', str(date.now().time())).group(1))
    
    def display_dataset(self):
        if self.dset:
            print(
"""
turntables:
[ ( o )/][|_|][ ( o )/]

calctables:
+----------+----------+
|   f(x)   |     x    |""")
            for k, v in dict(sorted(self.dset.iteritems(), key=operator.itemgetter(1))).iteritems():
                print("""+----------+----------+""")
                print(
                    ('|   %s'+(' '*(7-len(str(k))))+'|   %s'+(' '*(7-len(str(v))))) % (k,v)+'|')
            
            print("""+----------+----------+""")
            print(
                ('|  %s'+(' '*(8-len(self.kunit)))+'|  %s'+(' '*(8-len(self.vunit)))) % (self.kunit, self.vunit)+'|')
            print("""+----------+----------+""")
            print 'dataset acquired'
        else:
            print 'No dataset to display'
    
    def dataset_opts(self):
        try:
            print(
"""
-- Dataset commands:
    -- avgroc (avg rate of change)
    -- instroc (instantaneous rate of change)
    -- wq! (save and quit)
    -- q! (quit w/o saving)
""")
        except:
            print 'display error'

    def dataset_menu(self):
        try:
            while True:
                cmd = raw_input('ds>')
                if cmd in dscmds:
                    print getattr(self, cmd)()
                elif cmd == 'q!':
                    self.cleanup(dset=True)
                    print 'dataset removed'
                    break
                elif cmd == 'wq!':
                    print 'dataset saved'
                    break
                else:
                    print 'unknown command %s' % cmd
        except:
            return 'menu error'
        
    def avgroc(self):
        '''
        find average rate of change
        '''
        if self.x1 is None or self.x2 is None:
            try:
                self.x1 = float(raw_input('from>'))
                self.x2 = float(raw_input('to>'))
            except ValueError:
                return 'must be integer'
        for k, v in self.dset.iteritems():
            if float(v) == self.x1:
                f_of_x1 = float(k)
            elif float(v) == self.x2:
                f_of_x2 = float(k)
        
        try:
            self.avg = "(%s - %s)/(%s - %s)" % (f_of_x2,
                                                f_of_x1,
                                                self.x2,
                                                self.x1)
            return 'average rate of change is %s %s/%s' % (str(eval(self.avg)), self.kunit, self.vunit)
        except:
            return 'can\'t find rate of change. Insufficient values in dataset'
        finally:
            self.cleanup()
        
    def instroc(self):
        '''
        find instantaneous rate of change
        '''
        try:
            try:
                self.x = float(raw_input('at>'))
            except:
                return 'must be an integer'
            try:
                lower = [v for v in self.dset.values() if v < float(self.x)]
                higher = [v for v in self.dset.values() if v > float(self.x)]
                self.x1 = float(min(lower, key=lambda x:abs(float(x)-float(self.x))))
                self.x2 = float(min(higher, key=lambda x:abs(float(x)-float(self.x))))
            except:
                return 'can\'t find rate of change. Insufficient values in dataset'
                
            for k, v in self.dset.iteritems():
                if float(v) == self.x1:
                    f_of_x1 = float(k)
                elif float(v) == self.x2:
                    f_of_x2 = float(k)
            
            return 'instantaneous rate of change is %s %s/%s' % (str((f_of_x2 - f_of_x1) / (self.x2 - self.x1)),
                                                                 self.kunit,
                                                                 self.vunit)
        except:
            return 'error, review your submission'
            
        finally:
            self.cleanup()
    
    def derivative(self):
        try:
            dydx = []
            eq = ""
            if self.lim is None and self.x is None:
                try:
                    self.lim = f_of_x = raw_input("f(x)=")
                    self.x = fprime = raw_input("f'@")
                    for w in re.findall('(\w)', self.lim):
                        if w is not 'x':
                            try:
                                int(w)
                            except:
                                return 'unknown variable'
                        else:
                            pass
                    try:
                        int(self.x)
                    except ValueError:
                        return 'x must be an integer'
                        
                except:
                    return 'error handling the equation'
                    
            if self.sanitize() is False:
                return 'only integers and x'
            f_of_a = self.substitute_x(f_of_x, "("+str(float(fprime))+")")
            f_of_a_plus_x = self.substitute_x(
                f_of_x,"("+str(fprime)+'+1x)')
            self.lim = "(("+f_of_a_plus_x+")-("+f_of_a+"))/(1x)"
            self.x = 0
            return self.limit().replace('limit','derivative')
        except:
            return 'error, please review your submission'
        finally:
            self.cleanup()

    def limit(self):
        '''if f(x) is not defined, ask for it'''
        if self.lim is None or self.x is None:
            self.lim = raw_input('lim ')
            self.x = raw_input('x->')
        if self.lim is 'x':
            return 'limit is '+self.x
        if self.sanitize() is False:
            return 'only integers and x'
        self.format_equation()
        try:
            approaching = []
            side = 1
            x = self.x
            i = 0
            while i <= 7:
                if i is 6:
                    '''if we're approaching from the left,
                       then we're done'''
                    if side is -1:
                        break
                    '''if we're approaching from the right,
                       switch to the left'''
                    i = 0
                    side = -1
                    continue
                i += 1
                '''get .0001 more away from approaching int'''
                inc = float(.0001*i*side)
                eq = self.substitute_x(
                    self.lim, str(int(x)+inc))
                approaching.append(eval(eq))
                if self.opts['show_work'] is True:
                    print str(eq)+" = "+str(eval(eq))
                
            for l in approaching:
                '''if the difference from one limit
                   to the next is greater than one,
                   the limit does not exist'''
                if abs(l-approaching[-1]) > 1:
                    return 'limit does not exist'
            '''we found the limit'''
            if abs(round(approaching[1])-approaching[1]) < 1:
                return 'limit is '+str(round(approaching[1]))
            return 'limit is '+str(round(approaching[0], 2))
         
        except ZeroDivisionError:
            return 'no dividing by zero'
        except:
            return 'unforeseen error. please try again'
        finally:
            self.cleanup()
            
    def sanitize(self):
        ''''''
        if self.lim is None or self.x is None:
            return False
        lim = re.findall('(\w)', self.lim)
        for l in lim:
            try:
                if l is not 'x':
                    int(l)
                elif l is 'x':
                    pass
            except ValueError:
                self.cleanup()
                return False
        
        for i in str(self.x):
            try:
                int(str(i))
            except ValueError:
                self.cleanup()
                return False
               
        return True
            
    def cleanup(self, dset=False):
        self.lim = None
        self.x = None
        self.x1 = None
        self.x2 = None
        self.avg = None
        self.entered = False
        self.opts = {'show_work': False,
                     'new_dset': False}
        if dset:
            self.dset = {}
            self.kunit = None
            self.vunit = None

m = calculusME()
