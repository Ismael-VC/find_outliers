from __future__ import division


def median(data):
    if len(data) % 2 == 0:
        middle = int(len(data) / 2)
        n1, n2 = data[middle-1:middle+1]
        return (n1 + n2) / 2
    else:
        return data[int(len(data) / 2)]
        

def quartile_1(data):
    low_end = [item
               for item in sorted(data)
                   if item <= median(data)]
    return median(low_end)


def quartile_3(data):
    high_end = [item
                for item in sorted(data)
                    if item >= median(data)]
    return median(high_end)


def interquartile_range(Q1, Q3):
    return Q3 - Q1


def is_outlier(value, Q1, Q3, IQR):
    if not Q1 - (3.0 * IQR) < value < Q3 + (3.0 * IQR):
        return (True, 'Extreme')
    elif not Q1 - (1.5 * IQR) < value < Q3 + (1.5 * IQR):
        return (True, 'Mild')
    else:
        return (False, '')
        
        
def main():
    data = [2, 1, 10, 5, 30, 20, 40, 3, 5,
            6, 7 , 12, 13, 1000, 4, 7, 8,
            4, 3, 8, 9,5000, 50, 20, 33]
    data.sort()
    print 'Data:', data
    print 'Median:', median(data)
    
    Q1 = quartile_1(data)
    print 'Q1:', Q1
    
    Q3 = quartile_3(data)
    print 'Q3:', Q3        
    
    IQR = interquartile_range(Q1, Q3)
    print 'IQR:', IQR
    
    print 'Inner: [ {0} ... {1} ]'.format(Q1 - (1.5*IQR), Q3 + (1.5*IQR))    
    print 'Outer: [ {0} ... {1} ]'.format(Q1 - (3.0*IQR), Q3 + (3.0*IQR))
                       
    outliers = [(item, is_outlier(item, Q1, Q3, IQR)[1])
                for item in set(data)
                    if is_outlier(item, Q1, Q3, IQR)[0]]
    print 'Outliers:', outliers
    
    
if __name__ == '__main__':
    main()
