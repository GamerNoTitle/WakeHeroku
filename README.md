# WakeHeroku

[English](#English)

## 简体中文

### 如何使用

- Fork此项目
- 添加一个名为`GITHUB_TOKEN`的Token，并为赋予`repo`，`admin:repo_hook` ， `workflow`的权限
- 添加名为`SITE`的Secrets，内容为自己Heroku应用地址。多个请用英文逗号分隔，请手动加上`https://`或者`http://`

### 修改时间

修改时间直接修改`/.github/workflows/WakeupHeroku.yml`文件的cron表达式即可。

**时间是UTC时间，注意时差问题**

## English

### How to use?

- Fork this repo
- Add a token in name `GITHUB_TOKEN` and give the permissions of `repo`, `admin:repo_hook` and `workflow`
- Add a secret in your repo named `SITE` and input all your application link in it. If you have more than one, please split it in comma. Please add `http://` or `https://` manually!

### Change time

Just edit the time in cron format in file `/.github/workflows/WakeupHeroku.yml`

**The time is UTC time**