# 3DCNN
CNN and 3DCNN
reference:https://github.com/rysmarie/MotionRecognition/tree/master/

This code requires [UCF-101 dataset](http://crcv.ucf.edu/data/UCF101.php).
All of video files need to be put in a file.

Options of 3dcnn.py are as following:  
`--batch`   batch size, default is 128  
`--epoch`   the number of epochs, default is 100  
`--videos`  a name of directory where dataset is stored, default is UCF101  
`--nclass`  the number of classes you want to use, default is 101  
`--output`  a directory where the results described above will be saved  
`--color`   use RGB image or grayscale image, default is False  
`--skip`    get frames at interval or contenuously, default is True  
`--depth`   the number of frames to use, default is 10  
