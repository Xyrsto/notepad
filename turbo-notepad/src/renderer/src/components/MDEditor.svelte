<script lang="ts">
    import { Carta, MarkdownEditor } from 'carta-md'
    import { attachment } from '@cartamd/plugin-attachment'
    import { emoji } from '@cartamd/plugin-emoji'
    import { slash } from '@cartamd/plugin-slash'
    import { code } from '@cartamd/plugin-code'
    import './styles.scss'

    const carta = new Carta({
        sanitizer: false,
        theme: 'houston',
        extensions: [
            attachment({
                async upload(file: File) {
                    return 'some-url-from-server.xyz'
                },
                supportedMimeTypes: ['image/png', 'image/jpeg', 'image/gif', 'image/svg+xml']
            }),
            emoji(),
            slash(),
            code()
        ]
    })

    export let value = `This is an example inspired by [GitHub](https://github.com)
\`\`\`js
console.log('Hello, World!');
\`\`\``
</script>

<MarkdownEditor bind:value mode="tabs" theme="github" {carta} />
