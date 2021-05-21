TMP=new.svg 

echo "$1"circle_"$2".png
echo s/\#b3b3b3/"$2"/g

cp circle.svg $TMP
sed -i s/\#b3b3b3/"$2"/g $TMP
inkscape -z $TMP -w 16 -h 16 -e "$1"circle_"$2".png 

rm $TMP