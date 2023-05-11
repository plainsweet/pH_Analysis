# import module
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import time    
    
import streamlit as st
#pH-Analysis.py
st.image("https://adivapelajar.files.wordpress.com/2023/05/20230511_130815_0000.png?w=1024")    
with st.sidebar.container():
    st.image("https://adivapelajar.files.wordpress.com/2023/05/20230505_153644_0000.png?w=1024", width=250)
    

test = st.sidebar.selectbox("Navigation", ['Home', "About pH🧪", "About Us", "Contact Us"])
       
with st.sidebar.container():
    st.sidebar.markdown("Logtech - pH Analysis App")

if test == "Home":
    st.title(':blue[Aplikasi penentu pH Larutan]')
    st.markdown('''Hai users, selamat datang di web kami.😊''')
    st.markdown('''Aplikasi ini dapat digunakan untuk menentukan nilai pH dari suatu larutan atau sampel dengan menginput konsentrasi (Molaritas) .''')
        
    tombol=st.button('OLEH KELOMPOK 2')

    if tombol:
        st.write('Latifa Andjani')
        st.write('Muhamad Faris Adzikri')
        st.write('Raka Mulya Octama')
        st.write('Rakhmillah Fatikhannisa Ramadhiani')
        st.write('Siti Nurhaliza')
        
            
    tab1, tab2 = st.tabs(["Penentuan nilai pH", "Indikator"])

    with tab1:
        st.header('Penentuan nilai pH')
        NamaLarutan= st.text_input('Nama Larutan yang akan dihitung pH-nya:')
        st.write ('Silahkan pilih jenis larutan dengan format "asam kuat", "basa kuat", "asam lemah", "basa lemah"')
        option= st.selectbox('Jenis Larutan',("asam kuat", "basa kuat", "asam lemah", "basa lemah"))
        
        
        if option=="asam kuat":
                jumlah_digit=4
                cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
                jumlah_digit1=4
                val = st.number_input(f'Masukkan valensi larutan', format='%.'+str(jumlah_digit)+'f')
                H = cons * val
                import numpy as np
                pH = -(np.log10(H))
                if st.button('Hitung'):
                    st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                    st.subheader(f':green[{round(pH,2)}]')
                    st.balloons()
                else :
                    st.write()

        elif option=="basa kuat": 
                jumlah_digit=4 
                cons= st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
                jumlah_digit1=4 
                val = st.number_input(f'Masukan valensi larutan', format='%.'+str(jumlah_digit)+'f')
                OH = cons * val 
                import numpy as np 
                POH = (np.log10(OH))
                pH = 14-POH
                if st.button('Hitung'):
                    st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                    st.subheader(f':green[{round(pH,2)}]')
                    st.balloons()
                else :
                    st.write()


        elif option=="asam lemah": 
                jumlah_digit=4
                cons=st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f') 
                a = cons * (1.8 * 10**(-5))
                import numpy as np
                H = np.sqrt(a)
                pH = -(np.log10(H))
                if st.button('Hitung'):
                    st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                    st.subheader(f':green[{round(pH,2)}]')
                    st.balloons()
                else :
                    st.write()


        elif option=="basa lemah": 
                jumlah_digit=4
                cons=st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')  
                a = cons* (1.8 * 10**(-5))
                import numpy as np
                OH = np.sqrt(a)
                POH = - (np.log10(OH))
                pH = 14 - POH
                if st.button('Hitung'):
                    st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                    st.subheader(f':green[{round(pH,2)}]')
                    st.balloons()
                else :
                    st.write()

    
    with tab2:
        st.header("Penentuan indikator")
        jumlah_digit=1
        pH=st.number_input('Masukan nilai pH anda (range 1 - 14) :',float(jumlah_digit))

        if st.button('Submit'):
            if 1.0 <= pH <=4.4 :
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":orange[Sindur Metil (SM)]")

                st.write("---")

                st.subheader('Fakta Mengenai Sindur Metil (SM)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours-3.jpg', width=350)

                st.write('''Indikator sindur metil (SM) adalah suatu senyawa organometalik yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 3,1 - 4,4. Berikut adalah beberapa fakta menarik tentang indikator sindur metil :

1. Indikator sindur metil adalah senyawa organometalik pertama yang digunakan sebagai indikator pH pada larutan asam atau netral.

2. Warna indikator sindur metil berubah dari kuning ke merah tua ketika larutan menjadi asam.

3. Indikator sindur metil sangat stabil dan tidak terpengaruh oleh cahaya atau panas.

4. Senyawa ini sering digunakan dalam bidang kimia dan biologi sebagai indikator pH karena rentang perubahan warnanya sangat sempit dan akurat, serta tidak toksik dan mudah digunakan.

    ''')

                st.write(''':blue[Kelebihan : ]

1. Indikator sindur metil memiliki rentang perubahan warna yang akurat dan sempit, sehingga sangat cocok untuk digunakan dalam analisis kuantitatif.
2. Senyawa ini mudah digunakan dan tidak toksik, sehingga aman untuk digunakan dalam laboratorium.
3. Indikator sindur metil memiliki stabilitas yang baik terhadap cahaya dan panas, sehingga dapat bertahan dalam jangka waktu yang lama.
    ''')
                st.write(''':blue[Kekurangan : ]

1. Indikator sindur metil memiliki kelemahan yaitu rentang pH yang dapat diukur terbatas pada lingkungan yang bersifat basa.
2. Senyawa ini tidak dapat digunakan pada larutan yang bersifat sangat asam atau sangat basa, karena warnanya tidak akan berubah.
3. Indikator sindur metil rentan terhadap oksidasi dan degradasi, sehingga perlu disimpan dengan hati-hati dan digunakan dalam waktu yang singkat setelah dibuka.
    ''')

            elif 4.2 <= pH <=6.3 :
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":red[Metil Merah (MM)]")
                st.write("---")

                st.subheader('Fakta Mengenai Metil Merah (MM)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours-4.jpg', width=350)

                st.write('''Indikator metil merah (MM) adalah senyawa organik yang digunakan sebagai indikator pH pada larutan asam dan netral dalam rentang pH 4,2 - 6,3. Berikut adalah beberapa fakta menarik tentang indikator metil merah:

1. Indikator metil merah adalah salah satu jenis indikator pH yang paling umum digunakan dalam laboratorium kimia.

2. Warna indikator metil merah berubah dari merah jambu ke kuning ketika larutan menjadi asam.

3. Rentang perubahan warna indikator metil merah sangat lebar, sehingga dapat digunakan untuk melacak perubahan pH dalam larutan dengan rentang pH yang luas.

4. Warna merah jambu pada indikator metil merah berasal dari gugus metoksi (-OCH3) yang terdapat dalam strukturnya.

    ''')

                st.write(''':blue[Kelebihan : ]

1. Indikator metil merah memiliki perubahan warna yang sangat kontras dan mudah diamati, sehingga sangat mudah digunakan dalam laboratorium.
2. Senyawa ini memiliki harga yang terjangkau dan mudah ditemukan, sehingga sangat populer di laboratorium.
3. Indikator metil merah mudah larut dalam air dan pelarut organik lainnya, sehingga dapat digunakan pada berbagai jenis larutan.
    ''')
                st.write(''':blue[Kekurangan : ]

1. Tidak cocok untuk digunakan dalam analisis pH lingkungan yang bersifat basa.
2. Senyawa ini memiliki kelemahan yaitu rentan terhadap degradasi oleh cahaya dan panas, sehingga perlu disimpan dengan hati-hati dan digunakan dalam waktu yang singkat setelah dibuka.
3. Indikator metil merah rentan terhadap interferensi oleh ion logam seperti Fe3+ dan Al3+, sehingga perlu dilakukan kalibrasi kembali saat digunakan pada larutan yang mengandung ion logam tersebut.
    ''')



            elif 6.0 <= pH <=7.6 :
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":blue[Bromtimol Biru (BTB)]")
                st.write("---")

                st.subheader('Fakta Bromtimol Biru (BTB)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours-5.jpg', width=350)

                st.write('''Indikator bromtimol blue (BTB) adalah senyawa organik yang digunakan sebagai indikator pH pada larutan netral dan bersifat asam dalam rentang pH 6,0-7,6. Berikut adalah beberapa fakta menarik tentang indikator bromtimol blue:

1. Indikator bromtimol blue adalah salah satu jenis indikator pH yang paling umum digunakan dalam laboratorium kimia dan biologi.

2. Warna indikator bromtimol blue berubah dari kuning ke biru ketika larutan menjadi basa.

3. Indikator bromtimol blue sering digunakan dalam titrasi asam-basa karena perubahan warnanya yang tajam dan mudah diamati.

4. Rentang perubahan warna indikator bromtimol blue sangat sempit, sehingga cocok untuk digunakan dalam analisis kuantitatif.

    ''')

                st.write(''':blue[Kelebihan : ]

1. Indikator bromtimol blue memiliki perubahan warna yang tajam dan mudah diamati, sehingga sangat mudah digunakan dalam laboratorium.
2. Rentang perubahan warna indikator bromtimol blue sangat sempit, sehingga cocok untuk digunakan dalam analisis kuantitatif.
3. Indikator bromtimol blue mudah larut dalam air dan pelarut organik lainnya, sehingga dapat digunakan pada berbagai jenis larutan.
    ''')
                st.write(''':blue[Kekurangan : ]

1. Rentang pH yang dapat diukur oleh indikator bromtimol blue terbatas pada lingkungan netral dan asam, sehingga tidak cocok untuk digunakan dalam analisis pH lingkungan yang bersifat basa.
2. Senyawa ini memiliki kelemahan yaitu sensitivitas yang rendah terhadap perubahan pH pada lingkungan yang bersifat basa.
3. Indikator bromtimol blue rentan terhadap interferensi oleh ion logam seperti Fe3+ dan Al3+, sehingga perlu dilakukan kalibrasi kembali saat digunakan pada larutan yang mengandung ion logam tersebut.
    ''')

            elif 8.0 <= pH <=14 :
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":blue[Fenolftalein (PP)]")
                st.write("---")

                st.subheader('Fenolftalein (PP)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours-2.jpg', width=350)

                st.write('''Indikator fenolftalein (PP) adalah senyawa organik yang digunakan sebagai indikator pH pada larutan bersifat basa dalam rentang pH 8,0-10. Berikut adalah beberapa fakta menarik tentang indikator fenolftalein:

1. Indikator fenolftalein adalah salah satu jenis indikator pH yang paling umum digunakan dalam laboratorium kimia dan biologi.

2. Warna indikator fenolftalein berubah dari tidak berwarna menjadi merah muda ketika larutan menjadi basa.

3. Indikator fenolftalein sering digunakan dalam titrasi asam-basa karena perubahan warnanya yang tajam dan mudah diamati.

    Rentang perubahan warna indikator fenolftalein sangat sempit, sehingga cocok untuk digunakan dalam analisis kuantitatif.

    ''')

                st.write(''':blue[Kelebihan : ]

1. Indikator fenolftalein memiliki perubahan warna yang tajam dan mudah diamati, sehingga sangat mudah digunakan dalam laboratorium.
2. Rentang perubahan warna indikator fenolftalein sangat sempit, sehingga cocok untuk digunakan dalam analisis kuantitatif.
3. Indikator fenolftalein mudah larut dalam air dan pelarut organik lainnya, sehingga dapat digunakan pada berbagai jenis larutan.
    ''')
                st.write(''':blue[Kekurangan : ]

1. Tidak cocok untuk digunakan dalam analisis pH lingkungan yang bersifat netral atau asam.
2. Senyawa ini memiliki kelemahan yaitu sensitivitas yang rendah terhadap perubahan pH pada lingkungan yang bersifat netral atau asam.
3. Indikator fenolftalein rentan terhadap interferensi oleh ion logam seperti Fe3+ dan Al3+, sehingga perlu dilakukan kalibrasi kembali saat digunakan pada larutan yang mengandung ion logam tersebut.
    ''')

            else:
                st.error('Nilai yang anda masukkan salah, inputkan dalam range 3.1-10')

    
        
if test == "About pH🧪":
    st.title(':green[Yuk Mengenal Apa Itu pH]')
    
    tab1, tab2, tab3, tab4, = st.tabs(["About pH", "Skala pH", "Alat ukur", "Cara Kerja"])

    with tab1:
        

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://sciencenotes.org/wp-content/uploads/2022/02/Bronsted-Lowry-Acid-and-Base.png",width=300)

        with col2:
            st.image("https://rumusrumus.com/wp-content/uploads/2017/02/teori-asam-basa-bronsted-lowry.jpg",width=300)


        st.write('pH merupakan derajat keasaman yang digunakan untuk menyatakan tingkat keasaman atau kebasaan yang dimiliki oleh suatu larutan yang didefinisikan sebagai kologartitma aktivitas ion hidrogen (H+) yang terlarut. Koefisien aktivitas ion hidrogen tidak dapat diukur secara eksperimental, sehingga nilainya didasarkan pada perhitungan teoritis. Skala pH bukanlah skala absolut melainkan bersifat relatif.')
        st.write('Asam adalah larutan dengan pH dibawah 7. Menurut teori asam basa bronsted-lowry, asam didefinisikan sebagai zat yang mendonorkan proton [H+]. Asam kuat adalah larutan dengan pH rendah yang terionisasi secara sempurna dalam air. Asam kuat memiliki pH dibawah 3, tidak seperti asam lemah.Asam lemah hanya menyumbangkan sedikit ion hidrogennya atau hanya sekitar satu persennya yang terionisasi.')
        st.write('Basa kuat dan basa lemah adalah larutan yang memiliki pH diatas 7. Menurut teori asam basa bronsted-lowry, basa didefinisikan sebagai zat yang akseptor proton [H+]. Basa kuat adalah basa yang terionisasi secara sempurna kedalam air. Ketika larut dalam air, setiap molekul basa kuat akan melepas ion hidroksida (OH-). Basa kuat memiliki pH yang tinggi, biasanya lebih besar dari 11. Untuk basa lemah adalah larutan basa yang tidak terionisasi secara sempurna disalam air. Basa lemah memiliki pH sekitar 8 hingga 11')
        
        
        st.write("---")
        
        st.header(':blue[Playlist Tentang pH]')
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("pH in Everyday Life")
            st.video('https://www.youtube.com/watch?v=r3hirzlWILM')

        with col2:
            st.subheader("Chemistry Intro to pH and pOH")
            st.video('https://www.youtube.com/watch?v=LS67vS10O5Y&list=RDQMp9VJQh7mgqI&start_radio=1')

        with col3:
            st.subheader("What Are Indicators?")
            st.video('https://www.youtube.com/watch?v=xYQlvTblgCY&list=PLrJjlF85FHe1He0p7L1x-h2s92J9Gy8ca&index=3')

        st.write("---")
       
        
    
    with tab2:
        st.header("Skala pH")
        st.image("https://adivapelajar.files.wordpress.com/2023/05/20230505_170426_0000.png?w=1024", width=660)
        st.write("Skala pH adalah skala logaritmik yang digunakan untuk mengukur keasaman atau kebasaan (alkalinitas) suatu larutan. Skala ini berjalan dari 0 hingga 14, dengan nilai 7 sebagai titik netral. Semakin rendah nilai pH, semakin asam sifatnya. Sebaliknya, semakin tinggi nilai pH, semakin basa (alkaline) sifatnya. Setiap perbedaan satu satuan pada skala pH mewakili perbedaan sepuluh kali dalam keasaman atau kebasaan larutan. Contoh, suatu larutan dengan pH 3.0 adalah sepuluh kali lebih asam daripada larutan dengan pH 4.0. Begitu juga, larutan dengan pH 11.0 adalah sepuluh kali lebih basa daripada larutan dengan pH 10.0. Skala pH digunakan dalam berbagai aplikasi, seperti dalam industri makanan, kimia, dan farmasi, serta dalam analisis air dan tanah. Pengukuran pH dapat dilakukan menggunakan alat yang disebut pH meter atau dengan menggunakan indikator pH, seperti kertas lakmus atau fenolftalein.")
        
        import pandas as pd
        st.write('Beberapa contoh larutan serta jenisnya')
        data={'Nama larutan':['HCl','NaOH','Pb(OH)2','HNO3','HClO3','Cu(OH)2','LiOH','H2C2O4','RbOH','Ba(OH)2','H3PO4','CH3COOH','KOH','H2SO4','H2O2','NaHCO3','HBO3','HBr','HClO4','Fe(OH)2','NH4OH','H2CO3','Zn(OH)2'],
              'Jenis larutan':['Asam kuat','Basa kuat','Basa lemah','Asam kuat','Asam kuat','Basa lemah','Basa kuat','Asam lemah','Basa kuat','Basa kuat','Asam lemah','Asam lemah','Basa kuat','Asam kuat','Asam lemah','Basa lemah','Basa lemah','Asam kuat','Asam kuat','Basa lemah','Basa lemah','Asam lemah','Basa lemah']}

        df=pd.DataFrame(data)

        df

    with tab3:
     
        st.header("Alat ukur")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image('https://adivapelajar.files.wordpress.com/2023/05/png_20230506_125840_0000-1.png?w=768',width=230)
            st.caption('pH Meter')

        with col2:
            st.image("https://adivapelajar.files.wordpress.com/2023/05/png_20230506_130636_0000.png?w=768",width=230)
            st.caption('pH Universal')

        with col3:
            st.image("https://adivapelajar.files.wordpress.com/2023/05/png_20230509_164436_0000.png?w=798",width=230)
            st.caption('Kertas Lakmus')
        st.write('''pH meter adalah alat yang digunakan untuk mengukur pH suatu larutan atau zat dengan menggunakan elektroda pH yang peka terhadap perubahan konsentrasi ion H+ dalam larutan tersebut. Dalam penggunaannya, pH meter biasanya dilengkapi dengan layar digital yang menampilkan nilai pH secara akurat.

pH universal atau biasa juga disebut dengan pH indikator, adalah senyawa kimia yang dapat mengubah warna tergantung pada pH larutan yang diuji. Biasanya, pH universal digunakan untuk mengukur pH larutan yang memiliki rentang pH yang luas, seperti dalam penelitian kimia atau di laboratorium.

Sementara itu, kertas lakmus adalah kertas indikator yang digunakan untuk menguji pH larutan. Kertas lakmus mengandung zat kimia yang dapat bereaksi dengan ion H+ dalam larutan, sehingga dapat mengubah warnanya menjadi merah jika larutan bersifat asam, atau biru jika larutan bersifat basa.''')

        st.title("Apa itu Perbedaannya?")
        st.write('''Perbedaan utama antara ketiga alat tersebut adalah dalam metode pengukuran pH yang digunakan. pH meter menggunakan elektroda pH yang sangat akurat, sehingga hasil pengukuran pH lebih akurat dibandingkan dengan pH universal atau kertas lakmus. Namun, penggunaan pH meter memerlukan kalibrasi dan perawatan yang lebih rumit dan mahal.

pH universal dan kertas lakmus tidak memerlukan peralatan khusus dan lebih mudah digunakan, namun hasil pengukurannya tidak selengkap pH meter. pH universal menghasilkan rentang pH yang lebih luas, sedangkan kertas lakmus hanya dapat mengukur pH secara kasar dan terbatas pada asam atau basa saja.''')
            
            
    with tab4:
        st.header("Bagaimana cara menggunakan alat ukur pH?")
        st.write('''
        A. pH Meter:
        1. Disiapkan sampel yang akan di ukur kadar pHnya (letakkan dalam wadah).
        2. Dinyalakan dengan menekan tombol on pada pH meter.
        3. Dimasukkan pH meter ke dalam wadah yang berisi sampel/larutan yang akan di uji.
        4. Ditunggu hingga angka tersebut berhenti dan tidak berubah-ubah.
        5. Hasil akan terlihat di display digital.
        

        B. pH universal:
        1. Disiapkan sampel yang akan di ukur kadar pHnya (letakkan dalam wadah).
        2. Dimasukkan pH universal kedalam larutan yang akan di uji.
        3. Dibandingkan dengan skala yang terdapat pada tempat kertas pH universal
        4. Didapatkan pH dari larutan tersebut

        C. Kertas Lakmus:
        
        Kertas lakmus hanya dapat mengetahui apakah suatu larutan tersebut basa atau asam. Kita tidak dapat mengetahui berapa pH dari larutan tersebut.
            ''')
             
    
    
if test == "About Us":
    st.title(':green[Apa itu Logtech - pH Analysis App?]')
    
    st.subheader("Hello, to all user :wave:")
    
    st.write(
        "Logtech adalah sebuah web aplikasi yang didesign menentukan pH larutan secara otomamatis dan pencarian menarik tentang pH."
    )
    st.write("---")

    st.header("Apa yang Logtech lakukan")
    st.write("##")
    st.write(
            """
            Di Web Aplikasi pH Analisis ini, kita akan menyediakan untuk orang-orang yang:
            - sedang mencari nilai pH larutan.  
            - sedang mencari indikator pH yang tepat.
            - ingin belajar tentang apa itu pH.
            - ingin belajar tentang sejarah pH.
            - ingin belajar tentang alat pengukuran pH.
         
            Share web ini jika menarik dan bermanfaat bagi Anda 👍
            """
        )
    
    st.write("---")
    st.header("Our crew")
    st.image("https://adivapelajar.files.wordpress.com/2023/05/1683787364991.png?w=1181")
    
    
if test == "Contact Us":
    st.header(":mailbox: Get In Touch With Us!")
    contact_form = """
    <form action="https://formsubmit.co/rakastdy@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here"></textarea> 
        <button type="submit">Send</button>
        
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)
    
    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("logtech/style/style.css")
    

    
    
    



        
    



