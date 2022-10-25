#!/usr/bin/awk -f
# submit.sh

BEGIN { 
  RS="(###|###\n)";
  FS="---\n";
} {
  cmd="bash -c '"                         \
      "python3 "FILENAME".py <<EOT |\n"   \
       $1                                 \
      "EOT\n"                             \
      "diff -w -s - <(cat <<EOT\n"        \
       $2                                 \
      "EOT\n"                             \
      ")'"
  # print(cmd)
  system(cmd)
  print ""
}
