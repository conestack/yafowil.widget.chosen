import {importMapsPlugin} from '@web/dev-server-import-maps';
import {playwrightLauncher} from '@web/test-runner-playwright';

export default {
    nodeResolve: true,
    browsers: [
        playwrightLauncher({product: 'chromium'}),
    ],
    testFramework: {
        path: './node_modules/web-test-runner-qunit/dist/autorun.js',
        config: {
            noglobals: false
        }
    },
    files: [
        'js/tests/**/test_*.js',
    ],
    coverageConfig: {
        include: ['**/js/src/**/*.js'],
        exclude: ['**/node_modules/**', 'sources/**']
    },
    plugins: [
        importMapsPlugin({
            inject: {
                importMap: {
                    imports: {
                        // Import factory from jquery to allow access of global
                        // in chosen.jquery.js. See mockJQuery.js
                        'jquery-factory': './node_modules/jquery/dist/jquery.js',
                        'jquery': './js/tests/mockJQuery.js',
                        'chosen': './src/yafowil/widget/chosen/resources/chosen/chosen.jquery.js'
                    },
                },
            },
        }),
    ],
}
