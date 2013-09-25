#!/usr/bin/env python

import operator
import math
import re
from datetime import datetime as date

'''Calculus Made Easy'''

'''
import re
s = '(x+a)(x+b)(x+c)(x+d)'

fpat = '\((\w+)(\+|\-|\*|\/){1}(\w+)\)'

factors = re.findall(fpat, s)
refactor = []
ans = []

while len(factors) > 1:
    u1 = '%s*%s' % (factors[0][0], factors[1][0])
    u2 = '%s*%s' % (factors[0][0], factors[1][2])
    u3 = '%s*%s' % (factors[0][2], factors[1][0])
    u4 = '%s*%s' % (factors[0][2], factors[1][2])
    if factors[0] in refactor:
        refactor.remove(factors[0])
    factors.remove(factors[0])
    refactor += [(u1,u2,u3,u4)] + factors
    if len(factors) is 1:
        refactor.remove(factors[0])
        if factors[0] in refactor:
            refactor.remove(factors[0])
        factors.remove(factors[0])
    

print refactor

#!/usr/bin/env python

try:
    import re
except ImportError:
    print 'required library not installed'

class x:
    def __init__(self, var, pwr, coef, op):
        try:
            self.var = var
            self.pwr = int(pwr)
            self.coef = int(coef)
            self.op = op
        except ValueError:
            print 'wrong value types given'
            self = None
    
    def checkpwr(self):
        if self.pwr is 1:
            self.pwr = ''
        elif self.pwr is 0:
            self.pwr = ''
            self.var = '1'
        elif self.pwr is '' and self.coef is '':
            self.var = 0
        else:
            self.pwr = '^%s' % self.pwr
        return self
        
    def checkcoef(self):
        if self.coef is 1:
            self.coef = ''
        elif self.coef is 0:
            self.coef = ''
            self.var = 0
            self.pwr = ''
        return self
        
    def mul_div_behavior(self, p, op):
        try:
            if hasattr(p, 'var'):
                #if we're multiplying two variables
                if op is '*':
                    self.coef *= p.coef
                else:
                    self.coef /= p.coef
                self = self.checkcoef()
                if self.var is p.var:
                    #if the two variables are the same
                    if op is '*':
                        self.pwr += p.pwr
                    else:
                        self.pwr -= p.pwr
                    self = self.checkpwr().checkcoef()
                    return '%s(%s%s)' % (self.coef, self.var, self.pwr)
                else:
                    self = self.checkpwr().checkcoef()
                    p = p.checkpwr().checkcoef()
                    if self.var is 0 or p.var is 0:
                        return 0
                    else:
                        return '%s(%s%s)%s(%s%s)' % (self.coef, self.var, self.pwr, op, p.var, p.pwr)
                                              
            elif int(p):
                #if we're multiplying a variable by an integer
                if op is '*':
                    self.coef *= p
                else:
                    self.coef /= p
                self = self.checkcoef().checkpwr()
                return '%s%s%s' % (self.coef, self.var, self.pwr)
        except AttributeError:
            print 'exception raised at mul'
        
    def add_sub_behavior(self, p, op):
        try:
            if hasattr(p, 'var'):
                #if we're adding to variables
                if self.var is p.var:
                    #if we're adding to of the same variables
                    if self.pwr != p.pwr:
                        #if the vars have the same powers
                        self = self.checkpwr().checkcoef()
                        p = p.checkpwr().checkcoef()
                        if not self.op:
                            return ('(%s%s%s)%s(%s%s%s)' % (p.coef, p.var, p.pwr, op,
                                                           self.coef, self.var, self.var))
                        else:
                            return ('(%s%s%s)%s(%s%s%s)' % (self.coef, self.var, self.pwr,
                                                           op, p.coef, p.var, p.pwr))
                    else:
                        #the matching variables don't have same power
                        if op is '+':
                            self.coef += p.coef
                        else:
                            self.coef -= p.coef
                        self = self.checkpwr().checkcoef()
                        p = p.checkpwr().checkcoef()
                        return '%s%s%s' % (self.coef, self.var, self.pwr)
                                                   
            elif int(p):
                self = self.checkpwr().checkcoef()
                if not self.op:
                    return '%s%s%s%s%s' % (p, op, self.coef,
                                          self.var, self.pwr)
                else:
                    return '%s%s%s%s%s' % (self.coef, self.var, self.pwr,
                                          op, p)
                
        except:
            print 'except called @ add_sub'
        
    def pow_behavior(self, p):
        try:
            self.pwr = '^%s' % str(self.pwr*p)
            self.coef **= p
            return '%s%s%s' % (self.coef, self.var, self.pwr)
        except:
            print 'except raised @ pow'
        
    def __add__(self, p):
        return self.add_sub_behavior(p, '+')
        
    def __radd__(self, p):
        return self.add_sub_behavior(p, '+')
        
    def __sub__(self, p):
        return self.add_sub_behavior(p, '-')
        
    def __rsub__(self, p):
        return self.add_sub_behavior(p, '-')
        
    def __mul__(self, p):
        return self.mul_div_behavior(p, '*')
    
    def __rmul__(self, p):
        return self.mul_div_behavior(p, '*')
        
    def __div__(self, p):
        return self.mul_div_behavior(p, '/')
        
    def __rdiv__(self, p):
        return self.mul_div_behavior(p, '/')
        
    def __pow__(self, p):
        return self.pow_behavior(p)


fpat = '((\^?\-?\d*)([a-zA-Z1-9]+)(\^(\-?\d+))?(\+|\-|\*|\/)?)'

def observe_x(old=False, solve=True):
    if old is False:
        eq = raw_input('eq>')
    else:
        eq = old
    xs = {}
    fpat = '((\^?\-?\d*)([a-zA-Z1-9]+)(\^(\-?\d+))?(\+|\-|\*|\/)?)'
    neweq = ''
    xgroups = re.findall(fpat, eq)
    print xgroups
    for i,xi in enumerate(xgroups):
        op = xi[5]
        try:
            if xi[1] is '^':
                coef = int(xi[2])
                neweq += '%s' % xi[0]
                continue
            coef = int(xi[0].replace(xi[5],''))
            neweq += '%s%s' % (coef, op)
            print 'evaluating int %s...' % xi[2]
            continue
        except:
            pass
        if xi[4]:
            pwr = xi[4]
        else:
            pwr = 1
        if xi[1]:
            coef = xi[1]
        else:
            coef = 1
        print 'neweq', neweq
        print 'eq', eq
        xs['x%s'%i] = x(xi[2], pwr, coef, xi[5])
        classpat = 'xs\["x%s"\](\+|\-|\*|\/)?' % i
        neweq += re.search(classpat, eq.replace(xi[0], 'xs["x%s"]%s'%(i,op),1)).group(0)
        eq = eq.replace(xi[0], '', 1)
    if solve:
        print neweq
        neweq = neweq.replace('^', '**')
        #try:
        expression = 'ans = %s' % neweq
        exec(expression)
        print expression
        print ans
        #except SyntaxError as e:
        #    print 'error: %s' % e.msg
    return neweq, xs

neweq, xs = observe_x()

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
