<?php

/*
 * CORS tanpa wildcard.
 * - Non-produksi: localhost/127.0.0.1 port berapa pun, plus origin "null"
 *   (web admin yang dibuka langsung dari file://).
 * - Produksi: hanya origin yang tertulis di CORS_ALLOWED_ORIGINS.
 * CORS_ALLOWED_ORIGINS berisi daftar origin yang dipisahkan koma.
 */
$isProduction = env('APP_ENV') === 'production';
$origins = env('CORS_ALLOWED_ORIGINS');

return [
    'paths' => ['api/*'],

    'allowed_methods' => ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],

    'allowed_origins' => $origins !== null
        ? array_values(array_filter(array_map('trim', explode(',', $origins))))
        : ($isProduction ? [] : ['null']),

    'allowed_origins_patterns' => $isProduction
        ? []
        : ['#^https?://(localhost|127\.0\.0\.1)(:\d+)?$#'],

    'allowed_headers' => ['Accept', 'Authorization', 'Content-Type', 'X-Requested-With'],

    'exposed_headers' => ['Content-Disposition'],

    'max_age' => 0,

    'supports_credentials' => false,
];
