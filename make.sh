#!/bin/bash
# make.sh

if [ -f $1.py ]; then
  echo "'"$1.py"' already exist."
  exit 1
fi

# 알고리즘 파일 생성
cat <<EOT > $1.py
# https://www.acmicpc.net/problem/$1

EOT

# 검사 파일 생성
# 예제 입력 N
# ---
# 예제 출력 N
# ...
cat <<'EOT' > $1
var result = ""
$('.sampledata').map((i,e) => {
  result+=e.innerHTML+(i%2 ? '###\n': '---\n')
})
var textarea = document.createElement('textarea');
textarea.value = result;
document.body.appendChild(textarea);
textarea.select();
textarea.setSelectionRange(0, 9999);  // 추가
document.execCommand('copy');
document.body.removeChild(textarea);
console.log(result)
EOT
vim $1
