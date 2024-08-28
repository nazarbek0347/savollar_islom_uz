from customtkinter import *
from bs4 import BeautifulSoup as bs
import requests

oyna=CTk()
oyna.geometry('700x700')
oyna.title('m._.nazarbek')


def find_id():
    try:
        # savol id sini topish
        entry_word=str(entry_question.get())
        search_word='+'.join(entry_word.split())
        url=requests.get(f'https://savollar.islom.uz/search?words={search_word}&page=1')
        id_soup=bs(url.content, 'html.parser')
        id_search1=id_soup.find('div', class_='container data_block')
        id_search2=id_search1.find('div',class_='question')
        found_id=id_search2.find('a').get('href')

        # savol text ini olish
        question_url=requests.get(f'https://savollar.islom.uz{found_id}')
        question_soup=bs(question_url.content,'html.parser')
        searching1=question_soup.find('div',class_='container data_block')
        searching2=searching1.find('div',class_='in_question')
        text_in_question_html=searching2.find('div',class_='text_in_question')
        text_in_question=text_in_question_html.get_text()

        
        # javobi text ini olish answer_in_question
        question_url=requests.get(f'https://savollar.islom.uz{found_id}')
        answer_soup=bs(question_url.content,'html.parser')
        search_answer1=answer_soup.find('div',class_='container data_block')
        search_answer2=search_answer1.find('div',class_='in_question')
        answer_in_question_html=search_answer2.find('div',class_='answer_in_question')
        anser_in_question=answer_in_question_html.get_text()
        label.configure(text=f'Savol: {text_in_question}\n\nJavob: {anser_in_question}')
        label.place(relx=0.5,rely=0.4,anchor='center')
        entry_question.place_forget()
        search_button.place_forget()
        restart.place(relx=0.5,rely=0.85,anchor='center')
        entry_question.delete(0,len(entry_question.get()))
    except AttributeError:
        label.configure(text='Savolga javob topilmadi!')
        label.place(relx=0.5,rely=0.4,anchor='center')
        entry_question.place_forget()
        search_button.place_forget()
        restart.place(relx=0.5,rely=0.85,anchor='center')
        entry_question.delete(0,len(entry_question.get()))


def kirish():
    label.place_forget()
    restart.place_forget()
    entry_question.place(relx=0.5,rely=0.3,anchor='center')
    search_button.place(relx=0.5,rely=0.55,anchor='center')
    button_kirish.place_forget()


button_kirish=CTkButton(oyna,text='Kirish',font=('Arial',50),command=kirish)
button_kirish.place(relx=0.5,rely=0.45,anchor='center')

entry_question=CTkEntry(oyna,placeholder_text='Savolingizni kiriting',font=('Arial',30),width=300)
search_button=CTkButton(oyna,text='Qidirish',font=('Arial',40),command=find_id)

label=CTkLabel(oyna,text='',font=('Arial',15),width=500, wraplength=550)

label.pack()

restart=CTkButton(oyna,text="Boshqa savol so'rash",font=('Arial',40),command=kirish)


oyna.mainloop()
