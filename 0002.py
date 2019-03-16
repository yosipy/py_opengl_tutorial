# OpenGLとGLFWをインポートします
from OpenGL.GL import *
import glfw


def main():
    # GLFW初期化
    if not glfw.init():
        return

    # ウィンドウを作成
    window = glfw.create_window(640, 480, 'Hello World', None, None)
    if not window:
        glfw.terminate()
        print('Failed to create window')
        return

    # コンテキストを作成
    glfw.make_context_current(window)

    # バージョンを指定
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    while not glfw.window_should_close(window):
        # バッファを指定色で初期化
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # バッファを入れ替えて画面を更新
        glfw.swap_buffers(window)

        # イベントを受け付けます
        glfw.poll_events()

    # ウィンドウを破棄してGLFWを終了
    glfw.destroy_window(window)
    glfw.terminate()


# Pythonのメイン関数はこんな感じで書きます
if __name__ == "__main__":
    main()
