import cleanup from 'rollup-plugin-cleanup';
import {terser} from 'rollup-plugin-terser';

const out_dir = 'src/yafowil/widget/chosen/resources';

const outro = `
window.yafowil = window.yafowil || {};
window.yafowil.chosen = exports;
`;

export default args => {
    let conf = {
        input: 'js/src/bundle.js',
        plugins: [
            cleanup()
        ],
        output: [{
            name: 'yafowil_chosen',
            file: `${out_dir}/widget.js`,
            format: 'iife',
            outro: outro,
            globals: {
                jquery: 'jQuery'
            },
            interop: 'default'
        }],
        external: [
            'jquery'
        ]
    };
    if (args.configDebug !== true) {
        conf.output.push({
            name: 'yafowil_chosen',
            file: `${out_dir}/widget.min.js`,
            format: 'iife',
            plugins: [
                terser()
            ],
            outro: outro,
            globals: {
                jquery: 'jQuery'
            },
            interop: 'default'
        });
    }
    return conf;
};
