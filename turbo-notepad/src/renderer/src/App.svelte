<script lang="ts">
    import MDEditor from './components/MDEditor.svelte'
</script>

<div class="fixed top-0 left-0 w-full h-full rounded-lg">
    <div class="absolute inset-0 bg-gray-800 bg-opacity-70 rounded-lg"></div>
    <div class="relative rounded-lg">
        <div class="bg-turbo-notepad-menu text-white py-2 px-4 flex justify-between items-center shadow-md rounded-t-lg">
            <div class="draggable-left" style="-webkit-app-region: drag;">
                <div class="text-lg font-bold">Turbo Notepad</div>
            </div>
            <div class="button-wrapper">
                <div class="inline-block mr-4 cursor-pointer px-3 py-1 rounded"><button>File</button></div>
                <div class="inline-block mr-4 cursor-pointer px-3 py-1 rounded"><button>Alt+F4 to Exit</button></div>
            </div>
        </div>
        <div class="z-10">
            <MDEditor/>
        </div>
    </div>
</div>

<style>
    @import 'tailwindcss/base';
    @import 'tailwindcss/components';
    @import 'tailwindcss/utilities';

    .bg-turbo-notepad-menu {
        background-color: #516365;
    }

    .draggable-left {
        flex: 1;
    }

    .opaque-background {
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5));
    }

    container {
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.5);
    }

    .button-wrapper > div:hover {
        background-color: #6C8284;
    }

</style>
