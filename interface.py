from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from datetime import datetime 

KV = '''                                             #Indica que é KV linguagem
FloatLayout:                                         #Indica o tipo de layout
    MDToolbar:
        pos_hint: {"center_y": 0.95}
        title: "Calculadora de porcentagem a repassar para o Dentista"
   
    MDIconButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        icon: 'tooth-outline'
        user_font_size: '75sp'        
    
    MDRaisedButton:                                  #Indica o tipo de Botão
        text: 'Calcular'                             #Indica o texto do Botão
        size_hint_x: 0.3                             #Indica o tamanho de botão no eixo x
        size_hint_y: 0.1                             #Indica o tamanho de botão no eixo y
        pos_hint:{"center_x": 0.8, "center_y": 0.07}  #Indica a localização do Botão
        on_release: app.abrir_card()                 #Criamos aqui um método para chamar abrir card
    
    MDTextField:
        hint_text:'Data:'
        pos_hint:{"center_x": 0.2, "center_y": 0.68}
        size_hint_x: 0.3                             
        size_hint_y: 0.1 
        
    MDTextField:
        hint_text:'Nome do Paciente:'
        pos_hint:{"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.9
        
    MDTextField:
        hint_text:'Valor Pago R$:'        
        pos_hint:{"center_x": 0.2, "center_y": 0.5}
        size_hint_x: 0.3                             
        size_hint_y: 0.1 
        input_filter: 'float'
   
    MDLabel:
        text:'Dinheiro'
        pos_hint: {'center_y': .4}
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .1, 'center_y': .4}
        on_active: app.checkbox_dinheiro()
    
    MDLabel:
        text:'Débito'
        pos_hint: {'center_y': .36}                              #Escolher método de pagamento
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .1, 'center_y': .36}
        on_active: app.selecionar_debito()
   
    MDLabel:
        text:'Crédito a vista'
        pos_hint: {'center_y': .32}
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .15, 'center_y': .32}
        on_active: app.selecionar_creditoavista()

    MDLabel:
        text:'Crédito até 6x'
        halign:'center'
        pos_hint: {'center_y': .4}
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .59, 'center_y': .4}
        on_active: app.selecionar_credito6()
   
    MDLabel:
        text:'Crédito até 12x'
        halign:'center'
        pos_hint: {'center_y': .36}    
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .59, 'center_y': .36}
        on_active: app.selecionar_credito12()

    MDLabel:
        text:'Débito Elo'
        halign:'center'
        pos_hint: {'center_y': .32}
    
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .59, 'center_y': .32}
        on_active: app.selecionar_debitoelo()

    MDLabel:
        text:'Crédito a vista Elo'
        halign:'right'
        pos_hint: {'center_y': .4}
    
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .82, 'center_y': .4}
        on_active: app.selecionar_creditoelo()
    
    MDLabel:
        text:'Crédito até 6x Elo'
        halign:'right'
        pos_hint: {'center_y': .36}
    
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .82, 'center_y': .36}
        on_active: app.selecionar_credito6()

    MDLabel:
        text:'Crédito até 12x Elo'
        halign:'right'
        pos_hint: {'center_y': .32}
        
    MDCheckbox:
        size_hint: None, None                              #Escolher método de pagamento
        size: "48dp", "48dp"
        pos_hint: {'center_x': .82, 'center_y': .32}
        on_active: app.selecionar_creditoelo12()

    MDRectangleFlatButton:
        text: "Clinica Geral"
        pos_hint: {'center_x': .2, 'center_y': .2}
    MDSwitch:
        pos_hint: {'center_x': .62, 'center_y': .2}         #Escolher se foi clinico geral ou Implantodontia
        on_active: app.selecionar_procedimentogeral()  
    
    MDRectangleFlatButton:
        text: "Implantodontia"
        pos_hint: {'center_x': .5, 'center_y': .2}
    MDSwitch:
        pos_hint: {'center_x': .3, 'center_y': .2}
        on_active: app.selecionar_implantodontia()
'''


class MyApp(MDApp):
    def checkbox_dinheiro(self):
        maq = 0
    
    def selecionar_debito(self):
        maq_debi = 0.0178
    
    def selecionar_creditoavista(self):
        maq_cred = 0.0294
    
    def selecionar_credito6(self):
        maq_cred6 = 0.0350
    
    def selecionar_credito12(self):
        maq_cred12 = 0.0370
    
    def selecionar_debitoelo(self):
        maq_deb_elo = 0.0304
    
    def selecionar_creditoelo(self):
        maq_cred_elo = 0.0409    
    
    def selecionar_credito6(self):
        maq_cred_elo6 = 0.0462
    
    def selecionar_creditoelo12(self):
        maq_cred_elo12 = 0.0509
        
    def selecionar_procedimentogeral(self):
        receita = 0.35 

    def selecionar_implantodontia(self):
        receita = 0.50

    def abrir_card(self):
        print("Calculando")   

    def build(self):
        return Builder.load_string(KV)



MyApp().run()