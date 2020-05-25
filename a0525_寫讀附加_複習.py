def main():
    outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\大蘋果.txt','w+')
    outfile.write('大蘋果\n')
    outfile.write('大橘子\n')
    outfile.write('大奇異\n')
    outfile.seek(0)
    data = outfile.read()
    print(data)
main()
