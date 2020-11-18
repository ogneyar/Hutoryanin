var gulp = require('gulp');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var browsersync = require('browser-sync').create();
var reload  = browsersync.reload;

function css(cb) {        
    gulp.src('./web/scss/style.scss')
        .pipe(sass({
            errorLogToConsole: true
        }))
        .on('error', console.error.bind(console))
        .pipe(autoprefixer({
            overrideBrowserslist: ['last 5 versions'],
            casdcade: false
        }))
        .pipe(gulp.dest('./web/static/css/'))
        .pipe(sass({
            outputStyle: 'compressed'
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./web/static/css/'));        
    cb();
}

function Sync() {
    browsersync.init({
        proxy: '127.0.0.1:8000',
        port: 3000,
		browser: "opera",
		open: 'external'
    });
}
function watch() {
    gulp.watch('./web/templates/**/*.html', gulp.parallel(reload, watch));
    gulp.watch('./web/scss/**/*.scss', gulp.series(css, gulp.parallel(reload, watch)));
}

gulp.task('default', gulp.series(css, gulp.parallel(Sync, watch)));
