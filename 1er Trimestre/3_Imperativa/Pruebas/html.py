archivo = open("index.html", "w+")
archivo.seek(0)
archivo.write("<!DOCTYPE html>\n"+ 
                "<html>\n"+
                "<head>\n"+
                input("Contenido Head:\n") + "\n" +
                "</head>\n"+
                "<body>\n"+
                "<h2>" + input("Contenido de H2: ") + "</h2>"+
                "<iframe id='inlineFrameExample'\n"+
                'title="Inline Frame Example"\n'+
                'width="800"\n'+
                'height="600"\n'+
                'src="https://www.openstreetmap.org/export/embed.html?bbox=-6.344298720359803%2C36.78638926571394%2C-6.337217688560487%2C36.79031591112556&amp;layer=mapnik">\n'+
                '</iframe>\n'+
                "</body>\n"+
                "</html>\n")
archivo.close()
