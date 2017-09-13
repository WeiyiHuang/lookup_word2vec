# lookup_word2vec

从facebook提供的已训练好的word2vec中文表中查询词语对应vector\\
处理过的前10000个词语的word2vec情况整理在文件zh_dict和zh_vec.pkl中\\
需注意：使用时内嵌到程序文件中，i/o操作置于全局，以免多次查询重复读写文件
