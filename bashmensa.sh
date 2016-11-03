#!/usr/bin/env bash



############### Config ##############################################

URL="http://www.studentenwerk-muenster.de/de/essen-a-trinken/mensen/mensa-am-ring"
PLANVZ="${HOME}/.mensascript"
#Create Dir if not exists
[ -d $PLANVZ ] || mkdir $PLANVZ


############### Strings ##############################################

#Increment it
VERSION=2

Tage[1]="Montag"
Tage[2]="Dienstag"
Tage[3]="Mittwoch"
Tage[4]="Donnerstag"
Tage[5]="Freitag"
Tage[6]="Samstag"
Tage[7]="Sonntag"


STage[1]="Mo"
STage[2]="Di"
STage[3]="Mi"
STage[4]="Do"
STage[5]="Fr"
STage[6]="Sa"
STage[7]="So"



GESCHLOSSEN="   -geschlossen-"
NICHTBEKANNT="    -unbekannt-"

TRENNER="-----------------------------------------------------"


DayIDs[1]="montag"
DayIDs[2]="dienstag"
DayIDs[3]="mittwoch"
DayIDs[4]="donnerstag"
DayIDs[5]="freitag"


MenuIDs[1]="_menu1"
MenuIDs[2]="_menu2"
MenuIDs[3]="_menu3"


function GetMenuAtDay()
{
 cat - | grep '<td id="'${DayIDs[$1]}${MenuIDs[$2]}'">' | sed 's/<[^<>]*>/\n/g' | sed '/^[ \t\s\r\n]*$/d' | awk '{for (f=1;f<NF;f++) printf $f" "; gsub("[0-9],","",$NF); gsub("[0-9]","",$NF);  print $NF}' | sed 's/,/, /g' | sed 's/  */ /g'  
}


############### Check if we need to download the mensaplan #########
thisweek=$(date +%W)
PLAN=${PLANVZ}"/mensa_"$(date +"%Y_%W")

VERSIONFILE=${PLANVZ}"/version"

NEEDDOWNLOAD=0

if test -e $VERSIONFILE ; then
  CURRENTVERSION=$(cat $VERSIONFILE)
else 
  echo $VERSION > $VERSIONFILE
  CURRENTVERSION=-1
  NEEDDOWNLOAD=1
fi


if [ $CURRENTVERSION -lt $VERSION ]; then
 NEEDDOWNLOAD=1
fi

if test -e $PLAN ; then
  if [ $NEEDDOWNLOAD -eq 1 ]; then
    rm $PLAN 
  fi
else 
  NEEDDOWNLOAD=1
fi



if [ $NEEDDOWNLOAD -eq 1 ]; then
  echo $VERSION > $VERSIONFILE
  tmpfile=$(mktemp)
  wget -O ${tmpfile} ${URL} &>/dev/null

  TagHeute=$(date +%u)
  WochenStart=$((1-$TagHeute))
  counter=1
  while [ $counter -le 5 ];  do
     modifier="--date=${WochenStart}days"
     today=$(date ${modifier} +%d.%m.%Y)
     Tag=$(date ${modifier} +%u)
    
     DAYSTRING=$(echo ${Tage[$Tag]} $today)
     MENU1=$(cat $tmpfile | GetMenuAtDay $counter 1)
     MENU2=$(cat $tmpfile | GetMenuAtDay $counter 2)
     MENU3=$(cat $tmpfile | GetMenuAtDay $counter 3)


     if [[ "$MENU1" == "" ]] || [[ "$MENU1" == "geschlossen" ]] ; then
           echo -e "$DAYSTRING\n\n\n\n" >> $PLAN
     else
       echo $DAYSTRING>> $PLAN
       echo $MENU1>> $PLAN
       echo $MENU2>> $PLAN
       echo $MENU3>> $PLAN
       echo >> $PLAN
     fi
    
     counter=$(($counter+1))
     WochenStart=$(($WochenStart+1))
  done

fi;

############## Output #############################

FormattedOut()
{
 while read FTag FDatum ; do
 read Menu1
 read Menu2
 read Menu3
 read empty

 echo "Mensa am ${FTag}, ${FDatum}"
 echo $TRENNER
 if [[ "$Menu1" == "" ]] ; then
  echo "$GESCHLOSSEN"
 else
  echo "   $Menu1"
  if [[ "$Menu2" != "" ]] ; then
    echo "   $Menu2"
    echo "   $Menu3"
  fi
 fi;
 echo -e -n "$@"
 done
}

LsOut()
{
 while read FTag FDatum ; do
 read Menu1
 read Menu2
 read Menu3
 read empty

 if [[ "$Menu1" != "" ]] ; then
  echo -e "${FDatum}\t1\t${Menu1}"
  if [[ "$Menu2" != "" ]] ; then
    echo -e "${FDatum}\t2\t${Menu2}"
    echo -e "${FDatum}\t3\t${Menu3}"
  fi
 fi;
 echo -e -n "$@"
 done
}


EssenAmTag()
{
  PLAN=${PLANVZ}"/mensa_"$(date $1 +"%Y_%W")

  if [ -e $PLAN ]; then
    TAGINDEX=$((($(date $1 +"%u")-1)*5+4))
    if [ $TAGINDEX -ge 25 ]; then
     #Samstags oder Sonntags
       today=$(date ${1} +%d.%m.%Y)
       Tag=$(date ${1} +%u)
       echo -e "${Tage[$Tag]} $today" | FormattedOut
    else
       cat $PLAN | head -n $TAGINDEX | tail -n 4 | FormattedOut
    fi;
  else
     #Unbekannt
       today=$(date ${1} +%d.%m.%Y)
       Tag=$(date ${1} +%u)
       echo -e "${Tage[$Tag]} $today\n${NICHTBEKANNT}" | FormattedOut
  fi;

}



############## Main ###############################################
if [ $# \> 0 ] ; then
 if [[ "$1" == "morgen" ]]; then
   echo
   EssenAmTag --date=tomorrow 
 elif [[ "$1" == "gestern" ]]; then
   echo
   EssenAmTag --date=yesterday
 elif [[ "$1" == "woche" ]]; then
   TagHeute=$(date +%u)
   WochenStart=$((1-$TagHeute))
   counter=1
   echo
   while [ $counter -le 5 ];  do
     EssenAmTag --date="${WochenStart}days"
     counter=$(($counter+1))
     WochenStart=$(($WochenStart+1))
     if [ $counter -le 5 ]; then  echo ; fi
   done;
 elif [[ "$1" == "all" ]]; then
    echo
    cat ${PLANVZ}"/mensa_"* | FormattedOut "\n"
    exit;
 elif [[ "$1" == "lsall" ]]; then
    cat ${PLANVZ}"/mensa_"* | LsOut
    exit;
 else
   EssenAmTag --date=$1
 fi
else 
 EssenAmTag
fi;
echo



