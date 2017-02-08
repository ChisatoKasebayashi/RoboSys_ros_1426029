# RoboSys_ros_1426029

##マイクで音を得たことを認知するパッケージ
 * start_julius.py  
 juliusの起動(認識した単語を下のreceive_dataに送る)  
 * receive_data.py  
 start_juliusで認識した単語を受け取とる(受け取ったフラグを下のprint.pyに送る)  
 * print.py  
 receive_data.pyで文字列を取得したことを認知  
