print('NAMA    : Muhammad Algazali')
print('NIM     : E1E1 19 032')
print('MATKUL  : Struktur Data')
print('_________________________________________________')
        
class entry:
    def __init__(self,name,score,timeg):
        self.name=name
        self.score=score
        self.timeg=timeg

    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def get_timeg(self):
        return self.timeg

class scoreboard:
    def __init__(self, kapasitas):
        self.kapasitas=kapasitas
        self.array=[[0,0,0]]*kapasitas

        self.arraybaru=self.array

    def get_kapasitas(self):
        return self.kapasitas

    def get_array(self, x):
            self.arraybaru[x]=self.arraybaru[x]
            return self.arraybaru[x]
        
    def get_array1(self, x):
            return self.arraybaru[x][0]
        
    def get_array2(self, x):
            return self.arraybaru[x][1]
        
    def get_array3(self, x):
            return self.arraybaru[x][2]
        
    def set_array(self, x, nilai1, nilai2, nilai3):
            self.x=x
            array_baru=[0,0,0]
            
            self.nilai1=nilai1
            self.nilai2=nilai2
            self.nilai3=nilai3

            print ('nilai self.nilai1 = ',self.nilai1)
            print ('nilai self.nilai2 = ',self.nilai2)
            print ('nilai self.nilai3 = ',self.nilai3)
            
            array_baru[0]=self.nilai1
            array_baru[1]=self.nilai2
            array_baru[2]=self.nilai3
            
            self.arraybaru[self.x][0]=array_baru[0]
            self.arraybaru[self.x][1]=array_baru[1]
            self.arraybaru[self.x][2]=array_baru[2]

            self.arraybaru[x]=self.arraybaru[self.x]
            return self.x,self.arraybaru[x]

harapan_terakhir=0

kapasitas=10

array=kapasitas+1
llist=[None]*array
llist[0]=['Dy1--Jeff Bzs',0,6]
llist[1]=['Dy2--Elon Msk',0,7]
llist[2]=['Dy3--Bernard ',0,8]
llist[3]=['Dy4--Bill Gts',0,2]
llist[4]=['Dy5--Warren B',0,1]
llist[5]=['Dy6--Mark Zuc',0,6]
llist[6]=['Dy7--Larry El',0,6]
llist[7]=['Dy8--larry Pg',0,3]
llist[8]=['Dy9--algazali',0,0]
llist[9]=['Dy10-dummy ke',0,0]
llist[10]=['data ksoong ',0,0] #llist.pop[10]

kurungan=0
while (kurungan==1):
    score_board=scoreboard(10)


    inisial=0
    while (inisial==0):
        
        print ('\nDaftar Menu :\n1. Tampilkan List\n2. Tambahkan Prestasi\n3. Keluar')
        a=int(input('Masukkan pilihan anda = '))
        if (a==1):
            print('\npilihan (1) Menampilkan List... :')
            i=(0)
            x='  '
            y=','
            z=' Menit'
            print('NO,Nama Pemain,Score Tertinggi,Waktu')
            kapasitas=score_board.get_kapasitas()
            while i < kapasitas:
                array1=score_board.get_array1(i)
                array2=score_board.get_array2(i)
                array3=score_board.get_array3(i)
                nomor=i+1
                print(nomor,x,array1,y,array2,y,array3)
                i+=1
                
        elif (a==2): 
                print('\npilihan (2) Menambahkan prestasi...:')

                x=str(input('masukkan nama       = '))
                y=int(input('masukkan score      = '))
                z=int(input('masukkan waktu      = '))

                score = entry(x,y,z)
                
                arr0=score.get_name()
                arr1=score.get_score()
                arr2=score.get_timeg()

                n = score_board.get_kapasitas
                ganti_array=score_board.set_array(n, arr0,arr1,arr2)
                print (ganti_array)
                
                    
                
        elif (a==3):
            inisial=1

        else:
            print('--Inputan anda salah--')
            tanya=str(input('Tetap dalam program ? (Y/N) ='))
            if tanya==('Y') or tanya==('y') or tanya==('yes') or tanya==('ya'):
                inisial=0
            else:
                inisial=1            

    print ('\n--Semoga hari anda menyenangkan !--')

'''k=kapasitas-1
                n=0
                scorebaru=arr[1]

                
                while (n<=k):
                    ilham=print(array[k][1])
                    score=arr[1]
                    
                    if ( score == ilham ):
                        array[k-1]=array[k]
                        k=k-1
                    else:
                        n=k+1
                    array[k]=scorebaru
                    '''

''' --- BATAS KURUNGAN ---  '''

while (harapan_terakhir==0):
     print ('\nDaftar Menu :\n1. Tampilkan List\n2. Tambahkan Prestasi\n3. Keluar')
     a=int(input('Masukkan pilihan anda = '))
     #print (llist)
     if (a==1):
        print('\npilihan (1) Menampilkan List... :')
        nomor=1
        pecah=0

        pusat=0
        
        while (nomor<=10):
            pusat=int(pusat)
            llist[10][1]=llist[(pusat)][1]
            print('peringkat ',nomor,'  = ',llist[(pusat)][0],'  : ',llist[(pusat)][1],'  : ',llist[(pusat)][2],'Menit ')    
            pusat=pusat+1
            nomor=nomor+1
            
     elif (a==2):
         print('\npilihan (2) Menambahkan prestasi...:')
         x=str(input('masukkan nama   = '))
         y=int(input('masukkan score  = '))
         z=int(input('masukkan waktu  = '))

         baru=[0,0,0]
         baru[0]=x
         baru[1]=y
         baru[2]=z
         banding=baru[1]
         jadi=9
         while (jadi>=0):
             dasar=llist[jadi][1]
             astaga=llist[jadi]
             if (dasar<=banding):
                 x=jadi+1
                 llist[x][0]=llist[(jadi)][0]
                 llist[x][1]=llist[(jadi)][1]
                 llist[x][2]=llist[(jadi)][2]
                 
                 llist[jadi][0]=baru[0]
                 llist[jadi][1]=baru[1]
                 llist[jadi][2]=baru[2]
                 jadi=jadi-1
                 
             else:
                 x=jadi+1
                 llist[x][0]=baru[0]
                 llist[x][1]=baru[1]
                 llist[x][2]=baru[2]

                 llist[(jadi)][0]=llist[(jadi)][0]
                 llist[(jadi)][1]=llist[(jadi)][0]
                 llist[(jadi)][2]=llist[(jadi)][0]
                 
                 llist[jadi]=dasar
                 jadi=0-1
         
     elif (a==3):
         harapan_terakhir=1

     else:
            print('--Inputan anda salah--')
            tanya=str(input('Tetap dalam program ? (Y/N) ='))
            if tanya==('Y') or tanya==('y') or tanya==('yes') or tanya==('ya'):
                harapan_terakhir=0
            else:
                harapan_terakhir=1            

print ('\n--Semoga hari anda menyenangkan !--')
    
    

        




