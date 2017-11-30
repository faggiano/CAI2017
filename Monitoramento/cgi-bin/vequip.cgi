#!/bin/bash
IFS=$'\n'
echo "content-type: text/html"
echo
echo    '<html>'
echo '<pre>'
echo            '<head>'
echo                    '<style>'
echo                            'table {'
echo                                    'border-collapse: collapse;'
echo                                    'border-spacing: 0;'
echo                                    'width: 100%;'
echo                                    'border: 1px solid #ddd;'
echo                            '}'
echo                            'th, td {'
echo                                    'text-align: left;'
echo                                    'padding: 8px;'
echo                            '}'
echo                            'tr:nth-child(even){background-color: #f2f2f2}'
echo                    '</style>'
echo            '</head>'
echo            '<body>'
echo                    '<form action=../pages/equip.html>'
echo                            '<fieldset>'
echo                                    '<legend>Monitor</legend>'
echo                                            '<div style="overflow-x:auto;">'
echo                                                    '<table>'
echo                                                            '<tr>'
echo                                                                    '<th>Descrição</th>'
echo                                                                    '<th>Localidade</th>'
echo                                                                    '<th>Usuário</th>'
echo									'<th>IP</th>'
echo                                                            '</tr>'
for x in $(cat equipments.csv) ; do
        echo '<tr>'
        for y in $(echo $x) ; do
                echo "<td>$(echo $y | cut -d';' -f1)</td>"
                echo "<td>$(echo $y | cut -d';' -f2)</td>"
                echo "<td>$(echo $y | cut -d';' -f3)</td>"
                echo "<td>$(echo $y | cut -d';' -f4)</td>"
        done
        echo '</tr>'
done
#for x in $(cat equipamentos.csv) ; do
#        echo '<tr>' >> teste.txt
#	echo $x >> teste.txt
#        for y in $(echo $x) ; do
#	echo $y >> teste.txt
#                echo "<td>$(echo $y | cut -d";" -f1)</td>" >> teste.txt
#                echo "<td>$(echo $y | cut -d";" -f2)</td>" >> teste.txt
#                echo "<td>$(echo $y | cut -d";" -f3)</td>" >> teste.txt
#                echo "<td>$(echo $y | cut -d";" -f4)</td>" >> teste.txt
#        done
#        echo '</tr>' >> teste.txt
#done
echo                                                    '</table>'
echo                                            '</div>'
echo                                    '<br><br><input type=submit value=Retornar>'
echo                            '</fieldset>'
echo                    '</form>'
echo            '</body>'
echo '</pre>'
echo    '</html>'
unset IFS
