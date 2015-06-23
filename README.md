wget http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-ulaw-current.tar.gz
mkdir asterisk-extra-sounds-en-ulaw-current-20150623
tar xvzf asterisk-extra-sounds-en-ulaw-current.tar.gz -C asterisk-extra-sounds-en-ulaw-current-20150623
tar cvzf asterisk-extra-sounds-en-ulaw-current-20150623.tar.gz asterisk-extra-sounds-en-ulaw-current-20150623
rm asterisk-extra-sounds-en-ulaw-current.tar.gz
rm asterisk-extra-sounds-en-ulaw-current-20150623 -rf
git add .
git cm 'Release 20150623'
