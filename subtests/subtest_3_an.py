import streamlit as st
import streamlit.components.v1 as components
import time

def show_live_timer_an(seconds_remaining):
    components.html(f"""
    <div style="font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; color: #d9534f; 
                background-color: #fdf7f7; padding: 10px 15px; border: 2px solid #d9534f; 
                border-radius: 8px; text-align: center; margin-bottom: 10px;">
        ⏱️ SISA WAKTU SUBTES 3 (AN): <span id="timer_display_an">--:--</span>
    </div>
    <script>
        var timeLeft = {seconds_remaining};
        function updateDisplay() {{
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            var displayM = m < 10 ? "0" + m : m;
            var displayS = s < 10 ? "0" + s : s;
            var elem = document.getElementById("timer_display_an");
            if (elem) {{ elem.innerHTML = displayM + ":" + displayS; }}
            if (timeLeft <= 0) {{ 
                if (elem) elem.innerHTML = "00:00 (WAKTU HABIS)"; 
                var buttons = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < buttons.length; i++) {{
                    if (buttons[i].innerText.includes('Simpan') || buttons[i].innerText.includes('Selesaikan')) {{
                        buttons[i].click();
                        break;
                    }}
                }}
            }} else {{ 
                timeLeft--; 
            }}
        }}
        updateDisplay();
        setInterval(updateDisplay, 1000);
    </script>
    """, height=75)

def render_subtest_3_an():
    if "step_an" not in st.session_state:
        st.session_state.step_an = "instruction"
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if st.session_state.step_an == "instruction":
        st.title("📑 Petunjuk Subtes 03: AN (Hubungan Kata / Analogi)")
        st.info("💡 Bacalah petunjuk dan contoh di bawah ini dengan teliti. **Timer belum berjalan di halaman ini.**")
        st.markdown("""
        ### Aturan Pengerjaan:
        Ditentukan 3 (tiga) kata. Antara kata pertama dan kata kedua terdapat suatu hubungan tertentu. Antara kata ketiga dan salah satu di antara lima kata pilihan harus pula terdapat hubungan yang sama itu.

        ---
        ### Contoh 03:
        **Hutan : pohon = tembok : ?**  
        a) batu bata | b) rumah | c) semen | d) putih | e) dinding  
        
        *Penjelasan:* Hubungan antara *hutan* dan *pohon* ialah bahwa hutan terdiri atas pohon-pohon. Maka hubungan antara *tembok* dan salah satu kata pilihan ialah bahwa tembok terdiri atas batu-batu bata. Oleh karena itu, jawaban yang benar ialah **a) batu bata**.

        ---
        ### Contoh Berikutnya:
        **Gelap : terang = basah : ?**  
        a) hujan | b) hari | c) lembab | d) angin | e) kering  
        
        *Penjelasan:* *Gelap* ialah lawan dari *terang*, maka untuk *basah* lawannya ialah *kering*. Maka jawaban yang benar ialah **e) kering**.
        """)
        st.markdown("---")
        if st.button("Mulai Kerjakan Subtes 3 🚀", type="primary"):
            st.session_state.step_an = "test"
            st.session_state.start_time_an = time.time()
            st.rerun()

    elif st.session_state.step_an == "test":
        st.title("🧠 Subtes 03: AN (Hubungan Kata)")
        
        elapsed = int(time.time() - st.session_state.start_time_an)
        remaining = max(0, 420 - elapsed)
        show_live_timer_an(remaining)

        if remaining <= 0:
            st.warning("⏰ Waktu Subtes 3 telah habis! Menyimpan jawaban dan mengalihkan ke Hasil Ujian Bagian 1...")
            for q_id in range(41, 61):
                if f"an_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"an_{q_id}"]
            time.sleep(1)
            st.session_state.page = "result"
            st.rerun()

        questions_an = [
            {"id": 41, "no": "41", "q": "Menemukan : menghilangkan = Mengingat : ?", "opts": ["a) menghapal", "b) mengenai", "c) melupakan", "d) berpikir", "e) memimpikan"]},
            {"id": 42, "no": "42", "q": "Bunga : jambangan = Burung : ?", "opts": ["a) sarang", "b) langit", "c) pagar", "d) pohon", "e) sangkar"]},
            {"id": 43, "no": "43", "q": "Kereta api : rel = Otobis : ?", "opts": ["a) roda", "b) poros", "c) ban", "d) jalan raya", "e) kecepatan"]},
            {"id": 44, "no": "44", "q": "Perak : emas = Cincin : ?", "opts": ["a) arloji", "b) berlian", "c) permata", "d) gelang", "e) platina"]},
            {"id": 45, "no": "45", "q": "Lingkaran : bola = Bujur sangkar : ?", "opts": ["a) bentuk", "b) gambar", "c) segi empat", "d) kubus", "e) piramida"]},
            {"id": 46, "no": "46", "q": "Saran : kepustakaan = Merundingkan : ?", "opts": ["a) menawarkan", "b) menentukan", "c) menilai", "d) menimbang", "e) merenungkan"]},
            {"id": 47, "no": "47", "q": "Lidah : asam = Hidung : ?", "opts": ["a) mencium", "b) bernapas", "c) mengecap", "d) tengik", "e) asin"]},
            {"id": 48, "no": "48", "q": "Darah : pembuluh = Air : ?", "opts": ["a) pintu air", "b) sungai", "c) talang", "d) hujan", "e) ember"]},
            {"id": 49, "no": "49", "q": "Saraf : penyalur = Pupil : ?", "opts": ["a) penyinaran", "b) mata", "c) melihat", "d) cahaya", "e) pelindung"]},
            {"id": 50, "no": "50", "q": "Pengantar surat : pengantar telegram = Pandai besi : ?", "opts": ["a) palu godam", "b) pedagang besi", "c) api", "d) tukang emas", "e) besi tempa"]},
            {"id": 51, "no": "51", "q": "Buta : warna = Tuli : ?", "opts": ["a) pendengaran", "b) mendengar", "c) nada", "d) kata", "e) telinga"]},
            {"id": 52, "no": "52", "q": "Makanan : bumbu = Ceramah : ?", "opts": ["a) penghinaan", "b) pidato", "c) kelakar", "d) kesan", "e) ayat"]},
            {"id": 53, "no": "53", "q": "Marah : emosi = Duka cita : ?", "opts": ["a) suka cita", "b) sakit hati", "c) suasana hati", "d) sedih", "e) rindu"]},
            {"id": 54, "no": "54", "q": "Mantel : jubah = wool : ?", "opts": ["a) bahan sandang", "b) domba", "c) sutra", "d) jas", "e) tekstil"]},
            {"id": 55, "no": "55", "q": "Ketinggian puncak : tekanan udara = ketinggian nada : ?", "opts": ["a) garpu tala", "b) sopran", "c) nyanyian", "d) panjang senar", "e) suara"]},
            {"id": 56, "no": "56", "q": "Negara : revolusi = Hidup : ?", "opts": ["a) biologi", "b) keturunan", "c) mutasi", "d) seleksi", "e) ilmu hewan"]},
            {"id": 57, "no": "57", "q": "Kekurangan : penemuan = Panas : ?", "opts": ["a) haus", "b) khatulistiwa", "c) es", "d) matahari", "e) dingin"]},
            {"id": 58, "no": "58", "q": "Kayu : diketam = Besi : ?", "opts": ["a) dipalu", "b) digergaji", "c) dituang", "d) dikikir", "e) ditempa"]},
            {"id": 59, "no": "59", "q": "Olahragawan : lembing = Cendekiawan : ?", "opts": ["a) perpustakaan", "b) penelitian", "c) karya", "d) studi", "e) mikroskop"]},
            {"id": 60, "no": "60", "q": "Keledai : kuda pacuan = Pembakaran : ?", "opts": ["a) pemadam api", "b) obor", "c) letupan", "d) korek api", "e) lautan api"]}
        ]

        for q in questions_an:
            st.markdown(f"**Soal {q['no']}.** {q['q']}")
            st.radio(
                f"Pilih Jawaban No. {q['no']}:",
                options=q['opts'],
                key=f"an_{q['id']}"
            )
            st.markdown("---")

        if st.button("Simpan & Selesaikan Bagian 1 🏁", type="primary"):
            for q_id in range(41, 61):
                if f"an_{q_id}" in st.session_state:
                    st.session_state.answers[q_id] = st.session_state[f"an_{q_id}"]
            st.session_state.page = "result"
            st.rerun()
