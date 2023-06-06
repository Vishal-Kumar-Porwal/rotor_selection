#!/bin/bash

rm rotors.txt


echo -n 'Enter the name of the molecule:'
read molecule

echo -n 'Enter the name and path of xyz file:'
read xyz_file                                                          

echo -n 'Enter the name and path of connection file:'
read connection_file

printf "$xyz_file\n$connection_file" | python3  rotors_selection.py 

echo 'creating com files'
    

while read line; do
    # 
    echo $line
    line_1=$(echo $line | rev | cut -c10-| rev | cut -c2- )
    echo $line_1
    line_2=$(echo $line_1 | sed 's/ /_/g')
    echo $line_2
 
    echo  '%nprocshared=8'                                                 >> rotor_scan_$molecule"_"$line_2.com
    echo  '%mem=112GB       '                                              >> rotor_scan_$molecule"_"$line_2.com
    echo  "%chk=rotor_scan_$molecule"_"$line_2.chk"                          >> rotor_scan_$molecule"_"$line_2.com
    echo  '#p opt=modredundant 6-311+g(2d,d,p) b2plypd3'                   >> rotor_scan_$molecule"_"$line_2.com
    echo  '               '                                                >> rotor_scan_$molecule"_"$line_2.com
    echo  "Scan $molecule rotors   :"  $line_2                             >> rotor_scan_$molecule"_"$line_2.com
    echo  '               '                                                >> rotor_scan_$molecule"_"$line_2.com
    echo  '0  1           '                                                >> rotor_scan_$molecule"_"$line_2.com
    cat $xyz_file                                                          >> rotor_scan_$molecule"_"$line_2.com
    echo '                '                                                >> rotor_scan_$molecule"_"$line_2.com
    echo $line                                                             >> rotor_scan_$molecule"_"$line_2.com
    echo '                '                                                >> rotor_scan_$molecule"_"$line_2.com
    echo '                '                                                >> rotor_scan_$molecule"_"$line_2.com
    


 
done < rotors.txt



