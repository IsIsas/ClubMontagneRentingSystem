var gulp = require('gulp');
var browserify = require('browserify'),
 babelify = require('babelify'),
 source = require('vinyl-source-stream');
gulp.task('default', function () {
 return browserify('./source/app.js')
 .transform(babelify)
 .bundle()
 .pipe(source('app.js'))
 .pipe(gulp.dest('./build/'));
});

gulp.task('default', function () {
 return browserify('./source/app.js')
 .transform(babelify)
 .bundle()
 .pipe(source('people.js'))
 .pipe(gulp.dest('./build/'));
});
