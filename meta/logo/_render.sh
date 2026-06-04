#!/bin/bash
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p _tmp
i=0
render_svg () {
  local out="$1"; local w="$2"; local h="$3"; local src="$4"
  i=$((i+1))
  rm -f "$PWD/$out"
  ( "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
      --user-data-dir="$PWD/_tmp/cd-$i" \
      --default-background-color=00000000 \
      --window-size="$w","$h" \
      --virtual-time-budget=4000 \
      --run-all-compositor-stages-before-draw \
      --screenshot="$PWD/$out" \
      "file://$PWD/$src" >/dev/null 2>&1 ) &
  local pid=$!
  local elapsed=0
  while kill -0 $pid 2>/dev/null; do
    sleep 1
    elapsed=$((elapsed+1))
    if [ $elapsed -ge 25 ]; then
      kill -9 $pid 2>/dev/null
      pkill -9 -P $pid 2>/dev/null
      break
    fi
  done
  wait $pid 2>/dev/null
  if [ -f "$PWD/$out" ]; then
    echo "OK  $out  (${w}x${h})"
  else
    echo "FAIL $out"
  fi
}

# Mark (transparent)
render_svg logo-mark.png         1024 1024 logo-mark.svg
render_svg logo-mark@2x.png      2048 2048 logo-mark.svg

# Dark variant (has built-in dark background)
render_svg logo-mark-dark.png    1024 1024 logo-mark-dark.svg
render_svg logo-mark-dark@2x.png 2048 2048 logo-mark-dark.svg

# Mono variant (transparent)
render_svg logo-mark-mono.png    1024 1024 logo-mark-mono.svg
render_svg logo-mark-mono@2x.png 2048 2048 logo-mark-mono.svg

# Horizontal (直接渲染 SVG，使用系统字体，无需外网)
render_svg logo-horizontal.png   1600 480  logo-horizontal.svg
render_svg logo-horizontal@2x.png 3200 960 logo-horizontal.svg

echo "all done"
