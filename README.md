## 程序类别

### 重命名文件
* rename_files
* rename_files_fix

### 选取特征点，制作特征矩阵
* 需要提前新建从pitch_01到24个csv文件
* read_dir_from_dir文件
* read_directory文件  ——  read_directory_files函数
* read_csv文件  ——  read_file_from_directory函数
* convert文件 ——  convert_to_pixel函数
* get_sample文件 —— get_patches函数，国字脸模型
* get_sample_fix   椭圆脸模型

### 合成多个pitch文件，制作训练矩阵
* make_matrix     合成一个大矩阵文件
* make_matrix_fix  合成一个大矩阵文件，同时有规律选择测试集

### 训练随机森林
* tree
* train_trees
* train_forest
* train_forest_xyz  训练三个角度的随机森林
* estimate_output   评测数据的准确性
