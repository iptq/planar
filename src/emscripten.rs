use std::os::raw;

type EmCallbackFunc = ::std::option::Option<unsafe extern "C" fn()>;
extern "C" {
    pub fn emscripten_set_main_loop(_: EmCallbackFunc, _: raw::c_int, _: raw::c_int);
}
