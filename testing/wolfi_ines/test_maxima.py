from maxima import find_maxima
import numpy as np

def test_simple_seq():
    exp = [2,4]
    x = [1,2,3,2,4,3,2]
    out = find_maxima(x)
    print (out)
    print (exp)
    assert out == exp
    
def test_shorter_seq():
    x = [1,2, 3]
    exp = [2]
    out = find_maxima(x)
    assert out == exp
    
    
def test_em_all_ab():

    x1 = [0, 1, 2, 1, 2, 1, 0]
    x2 = [-i**2 for i in range(-3, 4)]
    x3 = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    x4 = [4, 2, 1, 3, 1, 2]
    x5 = [4, 2, 1, 3, 1, 5]
    x6 = [4, 2, 1, 3, 1]
    
    out1 = find_maxima(x1)
    out2 = find_maxima(x2)
    #print (out2)
    out3 = find_maxima(x3)
    #print (out3)
    out4 = find_maxima(x4)
    #print (out4)
    out5 = find_maxima(x5)
    #print (out5)
    out6 = find_maxima(x6)
    #print (out6)
    
    exp1 = [2,4]
    exp2 = [3]
    exp3 = [16,78]
    exp4 = [0,3,5]
    exp5 = [0,3,5]
    exp6 = [0,3]
    
    assert out1 == exp1
    assert out2 == exp2
    assert out3 == exp3
    assert out4 == exp4
    assert out5 == exp5
    assert out6 == exp6
    
    
def test_em_all_d ():
    x11 = [1, 2, 2, 3, 1]
    x12 = [1, 3, 2, 2, 1]
    x13 = [3, 2, 2, 3]
    x14 = [2, 2, 1, 3]
    
    out11 = find_maxima(x11)
    #print (out11)
    out12 = find_maxima(x12)
    #print (out12)
    out13 = find_maxima(x13)
    #print (out13)
    out14 = find_maxima(x14)
    #print (out14)
    
    exp11 = [3]
    exp12 = [1]
    exp13 = [0,3]
    exp14 = [0,3]
    
    assert out11 == exp11
    assert out12 == exp12
    assert out13 == exp13
    assert out14 == exp14
    

    
    
    
    
    
    
    

