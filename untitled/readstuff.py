import mysql.connector


def main():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='co2data')
    c = conn.cursor()
    #c.execute('Select count(*) From co2')
    #numberOfRows=c.fetchone()[0]
    #print(numberOfRows)
    c.execute('SELECT * FROM co2')
    #data1 = list()
    drawChart(1, 2)
    #for row in data1:
    while True:
        row = c.fetchone()
        if row == None:
            break;
        print(row[0],row[1])



def drawChart(x,y):
    print(x)
    print(y)

if __name__ == '__main__':
    main()

