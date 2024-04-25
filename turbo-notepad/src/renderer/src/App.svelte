<script lang="ts">
    
</script>


<div class="fixed top-0 left-0 w-full h-full bg-gray-800 bg-opacity-60 rounded-b-lg">
    <div class="bg-gray-800 text-white py-2 px-4 flex justify-between items-center shadow-md rounded-t-lg" style="-webkit-app-region: drag">
        <div class="text-lg font-bold">Turbo Notepad</div>
        <div>
            <div class="inline-block mr-4 cursor-pointer transition duration-300 hover:bg-gray-700 px-3 py-1 rounded">
                File
            </div>
            <div class="inline-block mr-4 cursor-pointer transition duration-300 hover:bg-gray-700 px-3 py-1 rounded">
                Exit
            </div>
        </div>
    </div>
</div>

<style>
    @import 'tailwindcss/base';
    @import 'tailwindcss/components';
    @import 'tailwindcss/utilities';
  
    .opaque-background {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5));
    }

    container {
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.5);
    }
</style>