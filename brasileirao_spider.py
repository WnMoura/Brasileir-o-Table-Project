import scrapy
import pandas as pd



class BrasileiraoSpider(scrapy.Spider):
    name = 'brasileirao'
    start_urls = ['https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/']


    def parse(self, response):
        
        dados = []
        
        tabela = response.xpath("//div[contains(@class, 'tabela-ge')]/div[contains(@class, 'row')]/div[contains(@class, 'col-lg-8')]/table[contains(@class, 'table-hover')]//tbody")

        linhas = tabela.xpath(".//tr")
        
        for linha in linhas:
            
            posicao = linha.xpath(".//th[1]/text()").get()
            time = linha.xpath(".//td[@class='table__team']//a/text()").get()
            pontos = linha.xpath(".//td[3]/text()").get()
            jogos = linha.xpath(".//td[4]/text()").get()
            vitorias = linha.xpath(".//td[5]/text()").get()
            empates = linha.xpath(".//td[6]/text()").get()
            derrotas = linha.xpath(".//td[7]/text()").get()
            gols_pro = linha.xpath(".//td[8]/text()").get()
            gols_contra = linha.xpath(".//td[9]/text()").get()
            saldo_gols = linha.xpath(".//td[10]/text()").get()
  
            dados.append({
                    'Posição':posicao,
                    'Time':time,
                    'Pontos':pontos,
                    'Jogos':jogos,
                    'Vitorias':vitorias,
                    'Empates':empates,
                    'derrotas':derrotas,
                    'GP':gols_pro,
                    'GC':gols_contra,
                    'SG':saldo_gols
                    })
            
        df = pd.DataFrame(dados)
            
        excel_file = 'Tabela do Campeonato Brasileiro(10% Atualizado) .xlsx'
        df.to_excel(excel_file, index=False)
        print ('Tabela gerada com Exito')
             