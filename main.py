from flet import *
import flet as ft
from pytube import YouTube

body = Container(
    Stack([
        Image(
            src='darkcity.png'
        ),
        Container(
            Container(
                Column([
                    Row([
                   Text(
                       "Download Vídeo",
                       color='white',
                       weight='w700',
                       size=26,
                       text_align='center',
                   ),
                    ], alignment=MainAxisAlignment.CENTER),
                   TextField(
                       border_radius=15,
                       border=border.all(1,'#44f4f4f4'),
                       bgcolor='transparent',
                       hint_text='URL'
                   ) ,
                   Row([
                   ft.ElevatedButton(
                       'Baixar Vídeo',
                       color='black',
                       bgcolor='white',
                       width=170,
                       height=40
                       )
                   ],alignment=MainAxisAlignment.CENTER),
                ],alignment=MainAxisAlignment.CENTER),
                width=490,
                height=300,
                margin=margin.only(top=150),
                border_radius=18,
                blur=Blur(10,12,BlurTileMode.MIRROR),
                border=border.all(1,'#44f4f4f4'),
                alignment=alignment.center
            ),
            alignment=alignment.center
            
        )
    ])
)

def main (page):
    
    page.add(
        body
    )



ft.app(target=main)