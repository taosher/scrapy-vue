用Scrapy爬取[cn.vuejs.org](http://cn.vuejs.org)的教程页面，下载并生成`markdown`文件，放置于`md`目录中

1. 安装依赖包

   `pip install -r requirements.txt`

2. 安装虚拟环境

   ```bash
   pip install virtualenv
   ```

3. 创建虚拟环境

   ```bash
   virtualenv vs
   ```

4. 激活虚拟环境

   ```bash
   source ./ENV/Scripts/activate
   ```

5. 开始爬取

   ```bash
   scrapy runspider ./vuespider/vuespider/spiders/vuespider.py
   ```

6. 看看`md`这个目录，已经按顺序下载好Vue的教程啦！

