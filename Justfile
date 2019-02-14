build_wasm:
    env \
        EMMAKEN_CFLAGS="-s ERROR_ON_UNDEFINED_SYMBOLS=1 -s ASSERTIONS=1 -s WASM=1 -s USE_SDL=2 -O3 -o index.html" \
        cargo build -vv --release --target wasm32-unknown-emscripten
