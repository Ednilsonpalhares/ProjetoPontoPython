
from appPonto.models import RegistrarPonto,Funcionario

funcionario = Funcionario(username='11',first_name='jose',nome='Jose',email='jose@gmail.com',telefone='(84)99122-3323',matricula='11',password='123')
funcionario2 = Funcionario(username='12',first_name='valerio',nome='Valerio',email='valerio@gmail.com',telefone='(84)99122-0000',matricula='12',password='123')
funcionario3 = Funcionario(username='13',first_name='Marcos',nome='Marcos',email='marcos@gmail.com',telefone='(84)99100-3323',matricula='13',password='123')
funcionario4 = Funcionario(username='111',first_name='fernanda',nome='Fernanda',email='fernanda@gmail.com',telefone='(84)98122-3323',matricula='111',password='123')
funcionario5 = Funcionario(username='119',first_name='karol',nome='Karol',email='karol@gmail.com',telefone='(84)99122-3303',matricula='119',password='123')
funcionario.save()
funcionario2.save()
funcionario3.save()
funcionario4.save()
funcionario5.save()

registro01 = RegistrarPonto(entrada='2016-11-01 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro02 = RegistrarPonto(entrada='2016-11-02 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro03 = RegistrarPonto(entrada='2016-11-03 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro04 = RegistrarPonto(entrada='2016-11-04 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro05 = RegistrarPonto(entrada='2016-11-07 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro06 = RegistrarPonto(entrada='2016-11-08 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro07 = RegistrarPonto(entrada='2016-11-09 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro08 = RegistrarPonto(entrada='2016-11-10 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro09 = RegistrarPonto(entrada='2016-11-11 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro10 = RegistrarPonto(entrada='2016-11-14 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro11 = RegistrarPonto(entrada='2016-11-15 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro12 = RegistrarPonto(entrada='2016-11-16 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro13 = RegistrarPonto(entrada='2016-11-17 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro14 = RegistrarPonto(entrada='2016-11-18 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro15 = RegistrarPonto(entrada='2016-11-21 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro16 = RegistrarPonto(entrada='2016-11-22 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro17 = RegistrarPonto(entrada='2016-11-23 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro18 = RegistrarPonto(entrada='2016-11-24 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro19 = RegistrarPonto(entrada='2016-11-25 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro20 = RegistrarPonto(entrada='2016-11-28 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro21 = RegistrarPonto(entrada='2016-11-29 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)
registro22 = RegistrarPonto(entrada='2016-11-30 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario)

registro01.save()
registro02.save()
registro03.save()
registro04.save()
registro05.save()
registro06.save()
registro07.save()
registro08.save()
registro09.save()
registro10.save()
registro11.save()
registro12.save()
registro13.save()
registro14.save()
registro15.save()
registro16.save()
registro17.save()
registro18.save()
registro19.save()
registro20.save()
registro21.save()
registro22.save()

registro23 = RegistrarPonto(entrada='2016-11-01 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro24 = RegistrarPonto(entrada='2016-11-02 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro25 = RegistrarPonto(entrada='2016-11-03 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro26 = RegistrarPonto(entrada='2016-11-04 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro27 = RegistrarPonto(entrada='2016-11-07 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro28 = RegistrarPonto(entrada='2016-11-08 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro29 = RegistrarPonto(entrada='2016-11-09 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro30 = RegistrarPonto(entrada='2016-11-10 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro31 = RegistrarPonto(entrada='2016-11-11 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro32 = RegistrarPonto(entrada='2016-11-14 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro33 = RegistrarPonto(entrada='2016-11-15 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro34 = RegistrarPonto(entrada='2016-11-16 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro35 = RegistrarPonto(entrada='2016-11-17 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro36 = RegistrarPonto(entrada='2016-11-18 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro37 = RegistrarPonto(entrada='2016-11-21 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro38 = RegistrarPonto(entrada='2016-11-22 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro39 = RegistrarPonto(entrada='2016-11-23 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro40 = RegistrarPonto(entrada='2016-11-24 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro41 = RegistrarPonto(entrada='2016-11-25 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro42 = RegistrarPonto(entrada='2016-11-28 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro43 = RegistrarPonto(entrada='2016-11-29 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)
registro44 = RegistrarPonto(entrada='2016-11-30 08:00:00',saida='2016-12-11 17:00:00',local="Coordenação de Extensão ",funcionario=funcionario2)

registro23.save()
registro24.save()
registro25.save()
registro26.save()
registro27.save()
registro28.save()
registro29.save()
registro30.save()
registro31.save()
registro32.save()
registro33.save()
registro34.save()
registro35.save()
registro36.save()
registro37.save()
registro38.save()
registro39.save()
registro40.save()
registro41.save()
registro42.save()
registro43.save()
registro44.save()


registro45 = RegistrarPonto(entrada='2016-11-01 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro46 = RegistrarPonto(entrada='2016-11-02 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro47 = RegistrarPonto(entrada='2016-11-03 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro48 = RegistrarPonto(entrada='2016-11-04 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro49 = RegistrarPonto(entrada='2016-11-07 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro50 = RegistrarPonto(entrada='2016-11-08 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro51 = RegistrarPonto(entrada='2016-11-09 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro52 = RegistrarPonto(entrada='2016-11-10 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro53 = RegistrarPonto(entrada='2016-11-11 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro54 = RegistrarPonto(entrada='2016-11-14 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro55 = RegistrarPonto(entrada='2016-11-15 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro56 = RegistrarPonto(entrada='2016-11-16 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro57 = RegistrarPonto(entrada='2016-11-17 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro58 = RegistrarPonto(entrada='2016-11-18 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro59 = RegistrarPonto(entrada='2016-11-21 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro60 = RegistrarPonto(entrada='2016-11-22 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro61 = RegistrarPonto(entrada='2016-11-23 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro62 = RegistrarPonto(entrada='2016-11-24 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro63 = RegistrarPonto(entrada='2016-11-25 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro64 = RegistrarPonto(entrada='2016-11-28 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro65 = RegistrarPonto(entrada='2016-11-29 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro66 = RegistrarPonto(entrada='2016-11-30 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Acadêmica",funcionario=funcionario3)
registro45.save()
registro46.save()
registro47.save()
registro48.save()
registro49.save()
registro50.save()
registro51.save()
registro52.save()
registro53.save()
registro54.save()
registro55.save()
registro56.save()
registro57.save()
registro58.save()
registro59.save()
registro60.save()
registro61.save()
registro62.save()
registro63.save()
registro64.save()
registro65.save()
registro66.save()

registro66 = RegistrarPonto(entrada='2016-11-01 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro67 = RegistrarPonto(entrada='2016-11-02 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro68 = RegistrarPonto(entrada='2016-11-03 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro69 = RegistrarPonto(entrada='2016-11-04 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro70 = RegistrarPonto(entrada='2016-11-07 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro71 = RegistrarPonto(entrada='2016-11-08 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro72 = RegistrarPonto(entrada='2016-11-09 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro73 = RegistrarPonto(entrada='2016-11-10 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro74 = RegistrarPonto(entrada='2016-11-11 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro75 = RegistrarPonto(entrada='2016-11-14 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro76 = RegistrarPonto(entrada='2016-11-15 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro77 = RegistrarPonto(entrada='2016-11-16 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro78 = RegistrarPonto(entrada='2016-11-17 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro79 = RegistrarPonto(entrada='2016-11-18 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro80 = RegistrarPonto(entrada='2016-11-21 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro81 = RegistrarPonto(entrada='2016-11-22 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro82 = RegistrarPonto(entrada='2016-11-23 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro83 = RegistrarPonto(entrada='2016-11-24 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro84 = RegistrarPonto(entrada='2016-11-25 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro85 = RegistrarPonto(entrada='2016-11-28 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro86 = RegistrarPonto(entrada='2016-11-29 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro87 = RegistrarPonto(entrada='2016-11-30 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Extensão",funcionario=funcionario4)
registro66.save()
registro67.save()
registro68.save()
registro69.save()
registro70.save()
registro71.save()
registro72.save()
registro73.save()
registro74.save()
registro75.save()
registro76.save()
registro77.save()
registro78.save()
registro79.save()
registro80.save()
registro81.save()
registro82.save()
registro83.save()
registro84.save()
registro85.save()
registro86.save()
registro87.save()

registro88 = RegistrarPonto(entrada='2016-11-01 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro89 = RegistrarPonto(entrada='2016-11-02 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro90 = RegistrarPonto(entrada='2016-11-03 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro91 = RegistrarPonto(entrada='2016-11-04 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro92 = RegistrarPonto(entrada='2016-11-07 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro93 = RegistrarPonto(entrada='2016-11-08 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro94 = RegistrarPonto(entrada='2016-11-09 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro95 = RegistrarPonto(entrada='2016-11-10 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro96 = RegistrarPonto(entrada='2016-11-11 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro97 = RegistrarPonto(entrada='2016-11-14 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro98 = RegistrarPonto(entrada='2016-11-15 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro99 = RegistrarPonto(entrada='2016-11-16 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro100 = RegistrarPonto(entrada='2016-11-17 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro101 = RegistrarPonto(entrada='2016-11-18 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro102 = RegistrarPonto(entrada='2016-11-21 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro103 = RegistrarPonto(entrada='2016-11-22 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro104 = RegistrarPonto(entrada='2016-11-23 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro105 = RegistrarPonto(entrada='2016-11-24 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro106 = RegistrarPonto(entrada='2016-11-25 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro107 = RegistrarPonto(entrada='2016-11-28 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro108 = RegistrarPonto(entrada='2016-11-29 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro109 = RegistrarPonto(entrada='2016-11-30 08:00:00',saida='2016-12-11 17:00:00',local="secretaria Pesquisa",funcionario=funcionario5)
registro88.save()
registro89.save()
registro90.save()
registro91.save()
registro92.save()
registro93.save()
registro94.save()
registro95.save()
registro96.save()
registro97.save()
registro98.save()
registro99.save()
registro100.save()
registro101.save()
registro102.save()
registro103.save()
registro104.save()
registro105.save()
registro106.save()
registro107.save()
registro108.save()
registro109.save()